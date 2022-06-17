# -*- coding: utf-8 -*-
import moviepy.editor as mp
import os

query1 = 'assets/audioData/query-chan/konomichi.wav'
query2 = 'assets/audioData/query-chan/anoge-sen.wav'
query3 = 'assets/audioData/query-chan/ieie.wav'

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

        unity1 = 'outputs/audioData/#' + self.person_id + '/' + self.trialIndex + '/d1.wav'
        unity2 = 'outputs/audioData/#' + self.person_id + '/' + self.trialIndex + '/d2.wav'
        unity3 = 'outputs/audioData/#' + self.person_id + '/' + self.trialIndex + '/d3.wav'

        unity1Clip = mp.AudioFileClip(unity1)
        unity2Clip = mp.AudioFileClip(unity2)
        unity3Clip = mp.AudioFileClip(unity3)

        query1Clip = mp.AudioFileClip(query1)
        query2Clip = mp.AudioFileClip(query2)
        query3Clip = mp.AudioFileClip(query3)

        concat = mp.concatenate_audioclips([unity1Clip, query1Clip, unity2Clip, query2Clip, unity3Clip, query3Clip])

        clip = mp.VideoFileClip('assets/videoData/' + str(person_view) + 'pv.mp4').subclip()
        videoclip = clip.set_audio(concat)
        dir_path = 'outputs/videoData/#' + self.person_id
        os.makedirs(dir_path, exist_ok=True)
        videoclip.write_videofile(dir_path + '/' + self.trialIndex + '.mp4', codec='libx264',  audio_codec='aac', temp_audiofile='temp-audio.m4a', remove_temp=True)