# -*- coding: utf-8 -*-
from scipy.io import wavfile
import numpy as np
import pyworld as pw

class AudioConverter:
    audio_path = ''
    # ここ増やした方がいい
    # 初期化
    def __init__(self, audio_path):
        self.audio_path = audio_path
    def extractParameters(self):
        # 元データのf0, sp, apの取得を行う
        fs, data = wavfile.read(self.audio_path)
        data = data.astype(np.float)  # WORLDはfloat前提のコードになっているのでfloat型にしておく

        _f0, t = pw.dio(data, fs)  # 基本周波数の抽出
        f0 = pw.stonemask(data, _f0, t, fs)  # 基本周波数の修正
        sp = pw.cheaptrick(data, f0, t, fs)  # スペクトル包絡の抽出
        ap = pw.d4c(data, f0, t, fs)  # 非周期性指標の抽出
        # print(f0,sp,ap)
    # def convert(self):
    #     self.a = a
    #     self.b = b
    # def export(self):
    #     self.a = a
    #     self.b = b