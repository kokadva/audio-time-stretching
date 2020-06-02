from file_reader import FileReader
from file_writer import FileWriter


class WaveFile(object):

    def __init__(self, file_path):
        file_reader = FileReader(file_path)

        # Read the header
        self.file_path = file_path
        self.chunk_id = file_reader.next_string(4)
        self.chunk_size = file_reader.next_int(4)
        self.format = file_reader.next_string(4)
        self.subchunk_1_id = file_reader.next_string(4)
        self.subchunk_1_size = file_reader.next_int(4)
        self.audio_format = file_reader.next_int(2)
        self.num_channels = file_reader.next_int(2)
        self.sample_rate = file_reader.next_int(4)
        self.byte_rate = file_reader.next_int(4)
        self.block_align = file_reader.next_int(2)
        self.bits_per_sample = file_reader.next_int(2)
        file_reader.skip_bytes(self.subchunk_1_size - 16)  # Skip unused bytes
        self.subchunk_2_id = file_reader.next_string(4)
        self.subchunk_2_size = file_reader.next_int(4)
        self.bytes_per_sample = self.bits_per_sample // 8
        self.samples = []

        for channel in range(self.num_channels):
            self.samples.append([])

        while file_reader.has_next():
            channel_i = 0
            while channel_i < self.num_channels:
                self.samples[channel_i].append(file_reader.next_int(self.bytes_per_sample))
                channel_i += 1

    def save(self, output_file_path):
        # Write header
        file_writer = FileWriter(output_file_path)
        file_writer.start_writing()
        file_writer.write_string(self.chunk_id)
        file_writer.write_int(self.chunk_size, 4)
        file_writer.write_string(self.format)
        file_writer.write_string(self.subchunk_1_id)
        file_writer.write_int(self.subchunk_1_size, 4)
        file_writer.write_int(self.audio_format, 2)
        file_writer.write_int(self.num_channels, 2)
        file_writer.write_int(self.sample_rate, 4)
        file_writer.write_int(self.byte_rate, 4)
        file_writer.write_int(self.block_align, 2)
        file_writer.write_int(self.bits_per_sample, 2)
        file_writer.write_int(0, self.subchunk_1_size - 16)
        file_writer.write_string(self.subchunk_2_id)
        file_writer.write_int(self.subchunk_2_size, 4)

        # Write samples
        for k in range(len(self.samples[0])):
            for i in range(len(self.samples)):
                file_writer.write_int(self.samples[i][k], self.bytes_per_sample)
        file_writer.finish_writing()
