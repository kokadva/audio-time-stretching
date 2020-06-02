from OLA import slow_down
from WavFile import WaveFile
from utils import print_wave_file_header

if __name__ == '__main__':
    input_audio_file_path = 'audio-files/example.wav'
    output_audio_file_path = 'res.wav'
    wav_file = WaveFile(input_audio_file_path)
    print_wave_file_header(wav_file)
    slow_down(wav_file)
    wav_file.save(output_audio_file_path)
