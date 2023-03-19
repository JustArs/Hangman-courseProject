import tkinter as tk
from random import randint
from HangmanTerm import HangmanTerm as ht

root = tk.Tk()

root.title("Hangman")
root.geometry("1280x720")
root["bg"] = "#ffef9b"
root.resizable(width=False, height=False)

HangTxtImg = tk.PhotoImage(file = "splashscr.png")
Hangimg = tk.Label(root, image=HangTxtImg, bg="#ffef9b")
Hangimg.place(x=330, y=20)

def alphabetPrint():
    tk.Button(root, text = "A", font="Century 16").place(x=600,y=120)
    tk.Button(root, text = "B", font="Century 16").place(x=640,y=120)
    tk.Button(root, text = "C", font="Century 16").place(x=680,y=120)
    tk.Button(root, text = "D", font="Century 16").place(x=720,y=120)
    tk.Button(root, text = "E", font="Century 16").place(x=760,y=120)
    tk.Button(root, text = "F", font="Century 16").place(x=800,y=120)
    tk.Button(root, text = "G", font="Century 16").place(x=840,y=120)
    tk.Button(root, text = "H", font="Century 16").place(x=880,y=120)
    tk.Button(root, text = "I", font="Century 16").place(x=920,y=120)
    tk.Button(root, text = "J", font="Century 16").place(x=960,y=120)
    tk.Button(root, text = "K", font="Century 16").place(x=600,y=200)
    tk.Button(root, text = "L", font="Century 16").place(x=640,y=200)
    tk.Button(root, text = "M", font="Century 16").place(x=680,y=200)
    tk.Button(root, text = "N", font="Century 16").place(x=720,y=200)
    tk.Button(root, text = "O", font="Century 16").place(x=760,y=200)
    tk.Button(root, text = "P", font="Century 16").place(x=800,y=200)
    tk.Button(root, text = "Q", font="Century 16").place(x=840,y=200)
    tk.Button(root, text = "R", font="Century 16").place(x=880,y=200)
    tk.Button(root, text = "S", font="Century 16").place(x=920,y=200)
    tk.Button(root, text = "T", font="Century 16").place(x=960,y=200)
    tk.Button(root, text = "U", font="Century 16").place(x=680,y=300)
    tk.Button(root, text = "V", font="Century 16").place(x=720,y=300)
    tk.Button(root, text = "W", font="Century 16").place(x=760,y=300)
    tk.Button(root, text = "X", font="Century 16").place(x=800,y=300)
    tk.Button(root, text = "Y", font="Century 16").place(x=840,y=300)
    tk.Button(root, text = "Z", font="Century 16").place(x=880,y=300)

def gameProcess():
    mistakes = 5
    nx=600
    letters = ht()
    for i in letters:
        tk.Label(root, 
                 text="   ?   ",
                 bg="#ffef9b",
                 font=("Arial Bold", 20),
                 borderwidth=2,
                 relief="solid"
                 ).place(x=nx, y=460)
        nx+=80
    img_label = tk.Label(root, bg="#ffef9b")
    img_label.image = tk.PhotoImage(file="assets/h"+str(mistakes)+".png")
    img_label['image'] = img_label.image
    img_label.place(x=50, y=200)

    alphabetPrint()

def startPress():
    Hangimg.destroy()
    startBut.destroy()
    gameProcess()

startBut = tk.Button(text="START",
                     cursor="hand2",
                     activebackground="#ffca69",
                     bg="#ffef9b",
                     font="Century 45",
                     justify="center",
                     borderwidth=2,
                     relief="solid",
                     command=startPress
                     )
startBut.place(x=516,y=340)

root.mainloop()