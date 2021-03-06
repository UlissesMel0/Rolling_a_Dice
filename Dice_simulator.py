import tkinter
from PIL import Image, ImageTk
import random


window = tkinter.Tk()
window.geometry('400x400')
window.title('Rolling the dice!')


BlankLine = tkinter.Label(window, text="")
BlankLine.pack()


HeadingLabel = tkinter.Label(window, text="Hey Human! Let's play!",
                             fg="light green",
                             bg="Black",
                             font="Helvetica 16 bold italic")
HeadingLabel.pack()


dice = ['Side1.png', 'Side2.png', 'Side3.png', 'Side4.png', 'Side5.png', 'Side6.png']

DiceImage = ImageTk.PhotoImage(Image.open(random.choice(dice)))


ImageLabel = tkinter.Label(window, image=DiceImage)
ImageLabel.image = DiceImage


ImageLabel.pack(expand=True)


dice = ['Side1.png', 'Side2.png', 'Side3.png', 'Side4.png', 'Side5.png', 'Side6.png']


def rolling_dice():
    DiceImage = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    ImageLabel.configure(image=DiceImage)
    ImageLabel.image = DiceImage



button = tkinter.Button(window, text='Roll the Dice', fg='light green', bg='black', command=rolling_dice)

button.pack(expand=True)

window.mainloop()