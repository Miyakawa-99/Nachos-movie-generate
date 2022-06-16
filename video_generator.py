# -*- coding: utf-8 -*-
import moviepy.editor as mp
import os

class VideoGenerator:
    person_id = ''
    # data_astype = 'int16'
    audio_dir_path = ''
    trialIndex = '#0'
    # 初期化
    def __init__(self, person_id, trialIndex):
        self.person_id = person_id
        self.trialIndex = trialIndex
        self.audio_dir_path = 'outputs/audioData/#' + self.person_id + '#' + self.trialIndex
    def generate(self, person_view):
        # ここでオーディオクリップを作る
        unity1 = 'assets/audioData/unity-chan/konomichi.wav'
        unity2 = 'assets/audioData/unity-chan/anoge-sen.wav'
        unity3 = 'assets/audioData/unity-chan/ieie.wav'
        query1 = 'outputs/audioData/#' + self.person_id + '/' + self.trialIndex + '/d1.wav'
        query2 = 'outputs/audioData/#' + self.person_id + '/' + self.trialIndex + '/d2.wav'
        query3 = 'outputs/audioData/#' + self.person_id + '/' + self.trialIndex + '/d3.wav'

        unity1Clip = mp.AudioFileClip(unity1)
        unity2Clip = mp.AudioFileClip(unity2)
        unity3Clip = mp.AudioFileClip(unity3)

        query1Clip = mp.AudioFileClip(query1)
        query2Clip = mp.AudioFileClip(query2)
        query3Clip = mp.AudioFileClip(query3)

        concat = mp.concatenate_audioclips([unity1Clip, query1Clip, unity2Clip])

        clip = mp.VideoFileClip('assets/videoData/3pv.mp4').subclip()
        videoclip = clip.set_audio(concat)
        dir_path = 'outputs/videoData/#' + self.person_id
        os.makedirs(dir_path, exist_ok=True)
        videoclip.write_videofile(dir_path + '/' + self.trialIndex + '.mp4')