import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter.ttk import *
from PIL import ImageTk, Image

class HeardleHomeScreen:
    def __init__(self, callback):
        self.root = tk.Tk()
        self.root.title('Heardle')
        self.callback = callback
        self.titleLabel = Label(self.root, text="Heardle!", font=('Arial', 25))
        self.titleLabel.grid(row=0, column=0, columnspan=4, sticky='n')


        rock = Image.open('Images/Rock.png')
        rockimg = rock.resize((320, 320))
        self.rockPI = ImageTk.PhotoImage(rockimg)
        rap = PhotoImage(file = 'Images/Rap.png')
        self.rapPI = rap.subsample(2,2)
        self.buttonChoice()

    def buttonChoice(self):
        self.rockButton = Button(self.root, text='Rock', image = self.rockPI, compound = TOP, command=lambda: self.buttonClick('Rock'))
        self.rockButton.grid(row=1, column=1)
        self.rapButton = Button(self.root, text='Rap', image = self.rapPI, compound = TOP, command=lambda: self.buttonClick('Rap'))
        self.rapButton.grid(row=1, column=2)
        self.newButton = Button(self.root, text='New One', compound=BOTTOM)
        self.newButton.grid(row=2, column=1)
        self.anotherButton = Button(self.root, text='Another One', compound=BOTTOM)
        self.anotherButton.grid(row=2, column=2)
        # self.root.mainloop()

    def buttonClick(self, choice):
        self.choice = choice
        self.root.destroy()
        # self.callback(choice)
    def start(self):
        self.root.mainloop()
        return self.callback(self.choice)
    

# if __name__ == '__main__':
#     app = HeardleHomeScreen()
#     # app.mainloop()