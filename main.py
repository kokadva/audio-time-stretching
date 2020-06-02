from OLA import slow_down
from WavFile import WaveFile
from utils import print_wave_file_header

audio_file_path = 'audio-files/example.wav'
wav_file = WaveFile(audio_file_path)
print_wave_file_header(wav_file)
slow_down(wav_file)
wav_file.save('res.wav')


