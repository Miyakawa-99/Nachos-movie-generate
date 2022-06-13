# -*- coding: utf-8 -*-
import pandas as pd
from tools.terminal_interaction import confirmCreateMovie
from audio_converter import AudioConverter
          
# ここを変更する
PERSON_ID = 'A'


if confirmCreateMovie(person_id=PERSON_ID):
    audioConverter = AudioConverter(person_id=PERSON_ID)
    
    # 元データのf0, sp, apの取得を行う
    # audioConverter.extractParameters()

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
        print('f0: ' + str(f0) + ', sp: ' + str(sp) + ', ap: ' + str(ap) + ',pv: ' + str(pv))
        # ここで作る
        audioConverter.convert(param_ap=0.1, param_f0=1.0, param_sp=1.2, index = audioIndex)
        rowIndex += 1
    print("End")
