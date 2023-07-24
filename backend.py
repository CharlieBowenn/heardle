import time
import random
import simpleaudio
import os
from pydub import AudioSegment
from pydub.playback import play, _play_with_simpleaudio

print("Heardle!")
print("Enter a song name as a guess.\nEnter blank space to hear again.")
roundTimes = {
    1: 1,
    2: 2,
    3: 3,
    4: 5,
    5: 10,
    6: 15
}
choice = random.choice(os.listdir("Songs"))
song = AudioSegment.from_mp3(f'Songs/{choice}')
songname = choice[:-4]


def game():
    counter = 1
    correct = False
    while counter<7 and correct!=True:
        print(f"Round {counter}.\nYou have {roundTimes[counter]} seconds.")
        guess = round(counter)
        if guess.upper()==songname.upper():
            play(AudioSegment.from_mp3('Sounds/CorrectAnswer.mp3'))
            correct = True
        else:
            play(AudioSegment.from_mp3('Sounds/WrongAnswer.mp3'))
            counter+=1
    if correct==True:
        print(f"Congratulations! Song guessed in {counter} rounds.")
        play(AudioSegment.from_mp3('Sounds/GameWon.mp3'))
    else:
        print(f"Unlucky! The song was {songname}.")
        play(AudioSegment.from_mp3('Sounds/GameLost.mp3'))


def round(num):
    guessed = False
    while guessed != True:
        playSong(num)
        guess = input("Guess: ")
        if guess != "":
            guessed=True
        else:
            print("Playing again...")
    return guess


def playSong(num):
    playback = _play_with_simpleaudio(song)
    time.sleep(roundTimes[num])
    playback.stop()

def playSongg():
    playback = _play_with_simpleaudio(song)
    time.sleep(3)
    playback.stop()

# if __name__ == '__main__':
#     game()