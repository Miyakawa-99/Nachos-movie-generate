# -*- coding: utf-8 -*-
import pandas as pd
from tools.terminal_interaction import confirmCreateMovie
from audio_converter import AudioConverter
from tools.parameter_translate import parameterTranslate
          
# ここを変更する
PERSON_ID = 'A'

if confirmCreateMovie(person_id=PERSON_ID):
    audioConverter = AudioConverter(person_id=PERSON_ID)
    
    df = pd.read_csv('assets/order.csv')
    rowIndex = 0
    columnIndex = df.columns.get_loc('participant #' + PERSON_ID)
    while rowIndex < 54: # 54個生成する
        audioIndex = df.iat[rowIndex, columnIndex]
        f0 = df.iat[rowIndex, columnIndex + 1]
        sp = df.iat[rowIndex, columnIndex + 2]
        ap = df.iat[rowIndex, columnIndex + 3]
        pv = df.iat[rowIndex, columnIndex + 4]
        print('Start to generate ' + audioIndex +' audio data!')
        nf0, nap, nsp = parameterTranslate(f0 = f0, ap = ap, sp = sp)
        print('f0: ' + str(f0) + ' = ' + str(nf0.value) + ', sp: ' + str(sp) + ' = ' + str(nsp.value) + ', ap: ' + str(ap) + ' = ' + str(nap.value) + ', pv: ' + str(pv))
        # ここで作る
        audioConverter.convert(param_f0 = nf0.value, param_ap = nap.value, param_sp = nsp.value, index = audioIndex)
        print('Done !!!!!\n')
        rowIndex += 1
    print("End")
