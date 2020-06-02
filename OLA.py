
def slow_down(wav, speed=0.5):
    speed = 1 / speed
    output_samples = []
    for channel in range(wav.num_channels):
        output_samples.append([])

    def add_sample(sample, channel_id, index):
        if len(output_samples[channel_id]) <= index:
            output_samples[channel_id].append(0)
        output_samples[channel_id][index] = int((output_samples[channel_id][index] + sample) // speed)

    n = 500
    chunks_num = int((len(wav.samples[0]) // n) * speed - 1)
    for i in range(chunks_num):
        chunk_start_index = int(i * (n // speed))
        for k in range(chunk_start_index, chunk_start_index + n):
            for c in range(wav.num_channels):
                add_sample(wav.samples[c][k], c, n * i + (k - chunk_start_index))

        for k in range(chunk_start_index, chunk_start_index + n):
            for c in range(wav.num_channels):
                add_sample(wav.samples[c][k], c, int(n * i + n // speed) + (k - chunk_start_index))

    wav.samples = output_samples
    wav.subchunk_2_size = len(wav.samples[0])

