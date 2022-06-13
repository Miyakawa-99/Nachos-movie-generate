# Nachos実験用動画自動生成スクリプト

## ディレクトリ構成
- `assets/audioData/**.wav`
  - クローン/録音した入力データ
  - wavファイル (`'#'+id+'.wav'`形式)を想定
- `assets/videoData/**`
  - 音声なしのビデオデータ
  - 三人称視点と一人称視点の二つのデータが入っている
- `config.py`
  - F0, Ap, Spの値を指定しているところ
- `tools/terminal_interaction.py`
  - ターミナル出力部分

## 使い方

