# -*- coding: utf-8 -*-
from scipy.io import wavfile
import pyworld as pw

WAV_FILE = 'path_to_the_wav_file'

fs, data = wavfile.read(WAV_FILE)
data = data.astype(np.float)  # WORLDはfloat前提のコードになっているのでfloat型にしておく

_f0, t = pw.dio(data, fs)  # 基本周波数の抽出
f0 = pw.stonemask(data, _f0, t, fs)  # 基本周波数の修正
sp = pw.cheaptrick(data, f0, t, fs)  # スペクトル包絡の抽出
ap = pw.d4c(data, f0, t, fs)  # 非周期性指標の抽出

print(f0,sp,ap)