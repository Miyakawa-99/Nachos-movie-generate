# -*- coding: utf-8 -*-
from scipy.io import wavfile
import numpy as np
import pyworld as pw

class AudioConverter:
    person_id = ''
    # ここ増やした方がいい
    f0 = 0
    sp = 0
    ap = 0
    fs = 0
    # 初期化
    def __init__(self, person_id):
        self.person_id = person_id
        self._extractParameters()
    def _extractParameters(self):
        audio_path = 'assets/audioData/#' + self.person_id + '.wav' 
        # 元データのf0, sp, apの取得を行う
        self.fs, data = wavfile.read(audio_path)
        data = data.astype(np.float)  # WORLDはfloat前提のコードになっているのでfloat型にしておく

        _f0, t = pw.dio(data, self.fs)  # 基本周波数の抽出
        self.f0 = pw.stonemask(data, _f0, t, self.fs)  # 基本周波数の修正
        self.sp = pw.cheaptrick(data, self.f0, t, self.fs)  # スペクトル包絡の抽出
        self.ap = pw.d4c(data, self.f0, t, self.fs)  # 非周期性指標の抽出
        # print(f0,sp,ap)
    def convert(self, param_f0, param_ap, param_sp, index):
        # 記号と値の変換
        ## 要確認
        ## f0
        converted_f0 = self.f0 * param_f0
        ## ap
        converted_ap = self.ap * param_ap
        ## sp
        converted_sp = np.zeros_like(self.sp)
        for f in range(converted_sp.shape[1]):
            converted_sp[:, f] = self.sp[:, int(f/param_sp)]
        converted_audio = pw.synthesize(converted_f0, converted_sp, converted_ap, self.fs)  
        self._export(data=converted_audio, index = index)
    def _export(self, data, index):
        wavfile.write('outputs/audioData/' + self.person_id + index + '.wav', rate=self.fs, data=data)