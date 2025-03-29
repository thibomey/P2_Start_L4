from tkinter import messagebox

info = ["Dit is zeker geen virus", "Echt niet hoor", "Zeker niet!", "Toch wel!"]
for info in info:
    messagebox.showinfo("virus", info)