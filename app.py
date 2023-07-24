#Centralised file for integration of front & back end
# import backend
import frontend
import time
import random
import simpleaudio
import os
from pydub import AudioSegment
from pydub.playback import play, _play_with_simpleaudio


choice = random.choice(os.listdir("Songs"))
song = AudioSegment.from_mp3(f'Songs/{choice}')
songname = choice[:-4]
def playSongg():
    playback = _play_with_simpleaudio(song)
    time.sleep(3)
    playback.stop()

def gotAnswer(event, box):
    print(box.get())




if __name__=='__main__':
    root, frame = frontend.createGUI()
    frontend.initBox(frame, command=gotAnswer)
    frontend.initBut(frame, command=playSongg)
    root.mainloop()