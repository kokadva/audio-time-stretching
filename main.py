from OLA import slow_down
from WavFile import WaveFile
from utils import print_wave_file_header

audio_file_path = 'taunt.wav'
# audio_file_path = 'audio.wav'
wav_file = WaveFile(audio_file_path)
print_wave_file_header(wav_file)

slow_down(wav_file)
# wav_file.sample_rate = int(wav_file.sample_rate * 1.5)
wav_file.save('test.wav')


