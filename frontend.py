import tkinter as tk
from tkinter import ttk

class HeardleGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Heardle")

        self.frame = ttk.Frame(self.root)
        self.frame.pack(padx=10, pady=10)


        self.titleLabel = ttk.Label(self.frame, text="Heardle!")
        self.titleLabel.pack(padx=5, pady=5)
        self.guess1 = ttk.Label(self.frame, text='Guess 1: ')
        self.guess1.pack(padx=5, pady=5)
        self.guess2 = ttk.Label(self.frame, text='Guess 2: ')
        self.guess2.pack(padx=5, pady=5)
        self.guess3 = ttk.Label(self.frame, text='Guess 3: ')
        self.guess3.pack(padx=5, pady=5)
        self.guess4 = ttk.Label(self.frame, text='Guess 4: ')
        self.guess4.pack(padx=5, pady=5)
        self.guess5 = ttk.Label(self.frame, text='Guess 5: ')
        self.guess5.pack(padx=5, pady=5)
        self.guess6 = ttk.Label(self.frame, text='Guess 6: ')
        self.guess6.pack(padx=5, pady=5)
        self.guessLabels={
            1: self.guess1,
            2: self.guess2,
            3: self.guess3,
            4: self.guess4,
            5: self.guess5,
            6: self.guess6
        }

    def initBut(self, command):
        self.but = ttk.Button(self.frame, text="Listen", command=command)
        self.but.pack(padx=5, pady=5)

    def initBox(self, command):
        self.answer = ttk.Entry(self.frame)
        self.answer.pack(padx=5, pady=5)
        self.answer.bind("<Return>", lambda event: command(event, self.answer))

    def updateLabel(self, label, message):
        self.label.config(text=message)

# def getGuess():
#     return answer.get()

# def createGUI():
#     self.root = tk.Tk()
#     self.root.title("Heardle")

#     frame = ttk.Frame(self.root)
#     frame.pack(padx=10, pady=10)


#     self.titleLabel = ttk.Label(frame, text="Heardle!")
#     self.titleLabel.pack(padx=5, pady=5)
#     self.guess1 = ttk.Label(frame, text='Guess 1: ')
#     self.guess1.pack(padx=5, pady=5)
#     self.guess2 = ttk.Label(frame, text='Guess 2: ')
#     self.guess2.pack(padx=5, pady=5)
#     self.guess3 = ttk.Label(frame, text='Guess 3: ')
#     self.guess3.pack(padx=5, pady=5)
#     self.guess4 = ttk.Label(frame, text='Guess 4: ')
#     self.guess4.pack(padx=5, pady=5)
#     self.guess5 = ttk.Label(frame, text='Guess 5: ')
#     self.guess5.pack(padx=5, pady=5)
#     self.guess6 = ttk.Label(frame, text='Guess 6: ')
#     self.guess6.pack(padx=5, pady=5)
#     # global answer
#     # answer = ttk.Entry(frame)
#     # answer.pack(padx=5, pady=5)
#     # answer.bind("<Return>", getGuess)
#     # but = ttk.Button(frame, text="Play", command=addRow)
#     # but.pack(padx=5, pady=5)

#     return self.root, frame