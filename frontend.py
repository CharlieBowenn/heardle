import tkinter as tk
from tkinter import ttk

# def addRow():
#     titleLabel.config(text="It worked lmao")
#     newLabel = ttk.Label(frame, text='hehe')
#     newLabel.pack(padx=5, pady=5)
def initBut(frame, command):
    but = ttk.Button(frame, text="Listen Again", command=command)
    but.pack(padx=5, pady=5)

def initBox(frame, command):
    # global answer
    answer = ttk.Entry(frame)
    answer.pack(padx=5, pady=5)
    answer.bind("<Return>", lambda event: command(event, answer))

# def getGuess():
#     return answer.get()

def createGUI():
    root = tk.Tk()
    root.title("Heardle")

    frame = ttk.Frame(root)
    frame.pack(padx=10, pady=10)


    titleLabel = ttk.Label(frame, text="Heardle!")
    titleLabel.pack(padx=5, pady=5)
    guess1 = ttk.Label(frame, text='Guess 1: ')
    guess1.pack(padx=5, pady=5)
    guess2 = ttk.Label(frame, text='Guess 2: ')
    guess2.pack(padx=5, pady=5)
    guess3 = ttk.Label(frame, text='Guess 3: ')
    guess3.pack(padx=5, pady=5)
    guess4 = ttk.Label(frame, text='Guess 4: ')
    guess4.pack(padx=5, pady=5)
    guess5 = ttk.Label(frame, text='Guess 5: ')
    guess5.pack(padx=5, pady=5)
    guess6 = ttk.Label(frame, text='Guess 6: ')
    guess6.pack(padx=5, pady=5)
    # global answer
    # answer = ttk.Entry(frame)
    # answer.pack(padx=5, pady=5)
    # answer.bind("<Return>", getGuess)
    # but = ttk.Button(frame, text="Play", command=addRow)
    # but.pack(padx=5, pady=5)

    return root, frame