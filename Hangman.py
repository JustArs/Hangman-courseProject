import tkinter as tk
from random import randint
from HangmanTerm import HangmanTerm as ht

root = tk.Tk()

root.title("Hangman")
root.geometry("1280x720")
root["bg"] = "#ffef9b"
root.resizable(width=False, height=False)

HangTxtImg = tk.PhotoImage(file = "splashscr.png")
Hangimg = tk.Label(root, image=HangTxtImg, bg="#ffef9b",)
Hangimg.place(x=330, y=20)

def startPress():
    Hangimg.destroy()
    startBut.destroy()

startBut = tk.Button(text="START", 
                     borderwidth=0, 
                     cursor="hand2",
                     activebackground="#ffca69",
                     bg="#ffef9b",
                     font="Century 45",
                     justify="center",
                     command=startPress
                     )
startBut.place(x=516,y=340)

root.mainloop()