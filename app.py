#Centralised file for integration of front & back end
import backend
import frontend
import tkinter as tk
from tkinter import ttk
import time
import random
import simpleaudio
import os
from pydub import AudioSegment
from pydub.playback import play, _play_with_simpleaudio


# roundTimes = {
#     1: 1,
#     2: 2,
#     3: 3,
#     4: 5,
#     5: 10,
#     6: 15
# }
# choice = random.choice(os.listdir("Songs"))
# song = AudioSegment.from_mp3(f'Songs/{choice}')
# songname = choice[:-4]

# def playSongg():
#     playback = _play_with_simpleaudio(song)
#     time.sleep(3)
#     playback.stop()

# roundLabels = {
#     1: 'guess1',

# }

def gotAnswer(event, box):
    round = backend.getRound()
    guessResult = backend.checkGuess(box.get())
    if guessResult:
        GUI.guessLabels[round].config(text=box.get(), foreground='green')
        box.delete(0, tk.END)
        root.update()
        play(AudioSegment.from_mp3('Sounds/CorrectAnswer.mp3'))
        showAnswer('W', round)
    else:
        GUI.guessLabels[round].config(text=box.get(), foreground='red')
        box.delete(0, tk.END)
        root.update()
        play(AudioSegment.from_mp3('Sounds/WrongAnswer.mp3'))
        if round==6:
            showAnswer('L')
    

def showAnswer(gameResult, round=0):
    GUI.answer.destroy()
    GUI.but.destroy()
    root.update()
    GUI.answerLabel = ttk.Label(GUI.frame, text=backend.getSong(), foreground='blue')
    GUI.answerLabel.pack(padx=5, pady=5)
    root.update()
    if gameResult=='W':
        GUI.titleLabel.config(text=f'Congratulations! You won in {round}/6 rounds')
        root.update()
        play(AudioSegment.from_mp3('Sounds/GameWon.mp3'))
    else:
        play(AudioSegment.from_mp3('Sounds/GameLost.mp3'))
    # GUI.guessLabels[round].config(text=box.get())
    # print(box.get())

def buttonPressed():
    round = backend.getRound()
    backend.playSong(backend.roundTimes[round])

###############################CHECK IF ENTERED OPTION IS RIGHT; UPDATE ROUND NUMBER & TIME

if __name__=='__main__':
    GUI = frontend.HeardleGUI()
    GUI.initBox(command=gotAnswer)
    GUI.initBut(command=buttonPressed)
    root = GUI.root
    root.mainloop()