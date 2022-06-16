# -*- coding: utf-8 -*-
from scipy.io import wavfile
import numpy as np
import pyworld as pw
import math
from scipy import interpolate
import os

class AudioConverter:
    person_id = ''
    dialogueIndex = ''
    data_astype = 'int16'
    # ここ増やした方がいい
    f0 = 0
    sp = 0
    ap = 0
    fs = 0
    # 初期化
    def __init__(self, person_id, dialogueIndex):
        self.person_id = person_id
        self.dialogueIndex = str(dialogueIndex)
        self._extractParameters()
    def _extractParameters(self):
        audio_path = 'assets/audioData/#' + self.person_id + '/d' + self.dialogueIndex + '.wav' 
        # 元データのf0, sp, apの取得を行う
        self.fs, data = wavfile.read(audio_path)
        self.data_astype = data.dtype
        data = data.astype(np.float)  # WORLDはfloat前提のコードになっているのでfloat型にしておく

        _f0, t = pw.dio(data, self.fs)  # 基本周波数の抽出
        self.f0 = pw.stonemask(data, _f0, t, self.fs)  # 基本周波数の修正
        self.sp = pw.cheaptrick(data, self.f0, t, self.fs)  # スペクトル包絡の抽出
        self.ap = pw.d4c(data, self.f0, t, self.fs)  # 非周期性指標の抽出
        # print(f0,sp,ap)
    def convert(self, param_f0, param_ap, param_sp, trialIndex):
        # 記号と値の変換
        ## 要確認
        ## f0
        converted_f0 = self.f0 * param_f0
        ## ap
        converted_ap = self.ap * param_ap
        ## sp
        # f_new = f;
        # S = f.spectrogram;
        # fftsize = (size(S, 1) - 1) * 2;
        # w = (0:fftsize-1) * fs / fftsize;
        # w2 = w * 0.8; //0.8倍
        # for i = 1:size(S, 2)
        #     tmp = log(S(:, i));
        #     tmp = [tmp(:); tmp(end-1:-1:2)];
        #     tmp2 = interp1(w, tmp, w2, 'linear');
        #     f_new.spectrogram(:, i) = exp(tmp2(1:fftsize/2+1));
        # end
        # ここから昔の
        # converted_sp = np.zeros_like(self.sp)
        # for f in range(converted_sp.shape[1]):
        #     print(int(f/param_sp))
        #     converted_sp[:, f] = self.sp[:, int(f/param_sp)]
        converted_sp = self.sp
        # s = self.sp.spectrogram
        fftsize = (converted_sp.shape[1] - 1 )  * 2
        # fftsize = (size(S, 1) - 1) * 2
        print(fftsize)
        w = np.arange(0, fftsize-1) * self.fs / fftsize
        w2 = w * 0.8
        # for i in range(converted_sp.shape[1]):
        #     # tmp = math.log(converted_sp[:, i]) //いったんLogは忘れる
        #     # tmp = [tmp[:], tmp[end-1:-1:2]]
        #     # tmp2 = interp1(w, tmp, w2, 'linear')
        #     # converted_sp[:, i] = exp(tmp2[1:fftsize/2+1])
        #     # tmp = math.log(converted_sp[:, i]) //いったんLogは忘れる
        #     tmp = [converted_sp[:], converted_sp[converted_sp.shape[1]-1:-1:2]]
        #     tmp2 = interpolate.interp1d(w, tmp, w2, 'linear')
        #     converted_sp[:, i] = exp(tmp2[1:fftsize/2+1])
        # end
        converted_audio = pw.synthesize(converted_f0, self.sp, converted_ap, self.fs).astype(self.data_astype)
        self._export(data = converted_audio, trialIndex = trialIndex)
    def _export(self, data, trialIndex):
        dir_path = 'outputs/audioData/#' + self.person_id + '/' + trialIndex
        os.makedirs(dir_path, exist_ok=True)
        wavfile.write(dir_path + '/d' + self.dialogueIndex + '.wav', rate = self.fs, data = data)