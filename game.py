from tkinter import *
import random

root = Tk()
root.geometry("700x400")
root.title("Roll Dice")


label = Label(root, text="", font=("times", 260),bg="#572303", fg="white")

def roll():
    dice = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
    label.configure(text=f'{random.choice(dice)} {random.choice(dice)}')  
    label.pack()


button = Button(root, text="Let's roll....", width=40, height=5, font=10, bg="#00A0AE",fg="white",bd=2, command=roll)
button.pack(padx=10, pady=10)

label.pack()

root.mainloop()

