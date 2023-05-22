#open a wave file
import wave

file = wave.open('abc.wav')

print(file.getnframes())