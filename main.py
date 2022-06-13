from scipy.io import wavfile
import pyworld as pw

WAV_FILE = 'path_to_the_wav_file'

fs, data = wavfile.read(WAV_FILE)
data = data.astype(np.float)  # WORLDはfloat前提のコードになっているのでfloat型にしておく