import tkinter

window = tkinter.Tk()
window.title("GUI les")
window.geometry("300x200")

# label maken
label = tkinter.Label(window, text="Welkom bij mijn eerste GUI!")
label.pack()

# Functie om tekst van label aan te passen
def verander_tekst():
    label.config(text="Knop ingedrukt!")
def verander_tekst2():
    label.config(text="Welkom bij mijn eerste GUI!")

# Knop aanmaken
button = tkinter.Button(window, text="Klik op mij!", command=verander_tekst)
button.pack()
button2 = tkinter.Button(window, text="Reset!", command=verander_tekst2)
button2.pack()

window.mainloop()