import tkinter
from tkinter import colorchooser

window = tkinter.Tk()
window.title("Kleuren kiezer")
window.geometry("300x200")


def open():
    kleur = colorchooser.askcolor()[1]
    if kleur:
        button.config(bg=kleur)

# Knop aanmaken
button = tkinter.Button(window, text="Open kleueren kiezer", command=open)
button.pack()



window.mainloop()