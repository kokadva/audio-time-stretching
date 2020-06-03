from OLA.constants import CHUNK_SIZE


def set_speed(wav, speed=0.5):
    print("Slowing down by", speed)

    chunk_overlap_ratio = 1 / speed / 4

    """
        If the we divied the whole audio file into constant size chunks and each chunk would be
        cut out from every N / 2 index then there will be File_Size / CHUNK_SIZE * 2 but it may give us an extra
        two chunks so we subtract 2 (if you draw it and calculate it'll be easier to undesrtand but it's
        nothing important)
    """
    chunks_num = int((len(wav.samples[0]) // CHUNK_SIZE) * 2 - 2)

    """
        If you look closely after placing first chunk every next chunk adds samples number equal to the size of 
        overlaping (size of overlaping would be CHUNK_SIZE * chunk_overlap_ratio, size of the first chunk simply 
        CHUNK_SIZE and the quantity of the other chunks besides the first chunks_num - 1 plus we use 
        each one twise so we just multiply that value by two
    """
    samples_num = int(CHUNK_SIZE + (2 * chunks_num - 1) * CHUNK_SIZE * chunk_overlap_ratio)

    """
        Initialize the same strucute for the output as is for the input wav file (list consisting 
        of lists as many as there are channels, each list for the channel equal to the length of samples_num)
    """
    output_samples = []
    for channel in range(wav.num_channels):
        output_samples.append([0] * samples_num)

    """
        When we add data to the output samples we must choose starting point for the chunk to overlap, the first value 
        for it would be 0, then CHUNK_SIZE / chunk_overlap_ratio, then 2 * (CHUNK_SIZE / chunk_overlap_ratio) and on 
        the X'th time it'll be X * (CHUNK_SIZE / chunk_overlap_ratio) so this X will be our overlap_index
    """
    overlap_index = 0

    print("Progress: 0%", end="", flush=True)

    for chunk_index in range(chunks_num):

        print('\r', end='')
        print("Progress: {percent}%".format(percent=chunk_index / chunks_num * 100), end="", flush=True)

        chunk_start_index = int(chunk_index * CHUNK_SIZE // 2)

        # Every chunk is used twice
        for x in range(2):

            for k in range(chunk_start_index, chunk_start_index + CHUNK_SIZE):

                for channel_index in range(wav.num_channels):
                    target_sample_index_to_copy = int((overlap_index + x)
                                                      * CHUNK_SIZE * chunk_overlap_ratio
                                                      + (k - chunk_start_index))
                    output_samples[channel_index][target_sample_index_to_copy] = \
                        min(output_samples[channel_index][target_sample_index_to_copy] + wav.samples[channel_index][k],
                            255)

        overlap_index += 2

    wav.samples = output_samples
    # Change the file size in the header accoring to the result
    wav.subchunk_2_size = len(wav.samples[0]) * wav.bytes_per_sample

    print('\r', end='')
    print("Progress: 100%")
