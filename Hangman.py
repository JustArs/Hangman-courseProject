import tkinter as tk
from random import randint
from HangmanTerm import HangmanTerm as ht
from HangmanTerm import secret 

mistakes = 1
rightLets = 1
word = ht()
print(word)
newArr = []
for i in range(len(word)) :
    newArr.append("  ?  ")

clicked = {}
letters = {}

for i in range(97, 123): #all chars
    clicked[chr(i)] = 0
    letters[chr(i)] = None


root = tk.Tk()

root.title("Hangman")
root.geometry("1280x720")
root["bg"] = "#ffef9b"
root.resizable(width=True, height=True)

HangTxtImg = tk.PhotoImage(file = "splashscr.png")
Hangimg = tk.Label(root, image=HangTxtImg, bg="#ffef9b")
Hangimg.place(x=330, y=20)

def UpdateWidgets():
    secretTales()
    alphabetPrint()
    imgPrint()

def ClearScreen():
    for widget in root.winfo_children():
        widget.destroy()

def imgPrint():
    img_label = tk.Label(root, bg="#ffef9b")
    img_label.image = tk.PhotoImage(file="assets/h"+str(mistakes)+".png")
    print("file=assets/h"+str(mistakes)+".png")
    img_label['image'] = img_label.image
    img_label.place(x=50, y=70)

def secretTales():
    print(newArr)
    nx=600
    for i in newArr:
        tk.Label(root, 
                text=i,
                bg="#ffef9b",
                font=("Arial Bold", 20),
                borderwidth=2,
                relief="solid"
                ).place(x=nx, y=460)
        nx+=80

def checkToWin():
    global mistakes
    global word
    global newArr
    global rightLets
    if (mistakes == 9) or (rightLets == len(newArr)):
        ClearScreen()
        if mistakes == 9:
            tk.Label(root, text = "You lose!", font="Century 16", bg="#ffef9b").pack()
        elif rightLets == len(newArr):
            tk.Label(root, text = "You win!", font="Century 16", bg="#ffef9b").pack()
        word = ht()
        newArr = []
        for i in range(len(word)) :
            newArr.append("  ?  ")
        StartButPrint()
        imgPrint()
        rightLets = 1
        mistakes = 1
        for i in range(97, 123): #all chars
            clicked[chr(i)] = 0
            letters[chr(i)] = None



def FindLetterBack(letter):

    global newArr
    global mistakes
    global rightLets
    
    if letter in word:
        newArr = secret(letter, newArr, word)
        rightLets += 1   
        print(rightLets)
        return rightLets
    else:
        if mistakes < 9:
            mistakes += 1
            return mistakes


def FindLetterFront(letter):
    ClearScreen()
    UpdateWidgets()
    checkToWin()

def DisableLetter(letter):
    global letters
    global clicked
    clicked[letter] = 1
    letters[letter]["state"] = tk.DISABLED
   
def alphabetPrint():
    global letters
    global clicked
    
    for i in range(97, 123):
        a = i - 96
        letters[chr(i)] = tk.Button(root, text = chr(i), font="Century 16")
        letters[chr(i)]['command'] = lambda arg=chr(i) : [DisableLetter(arg), FindLetterBack(arg), FindLetterFront(arg)]
        if clicked[chr(i)]:
            letters[chr(i)]["state"] = tk.DISABLED
        
        if a <= 9:
            letters[chr(i)].place(x = 560 + a * 50, y = 100)
        elif a <=18:
            a = i-105
            letters[chr(i)].place(x = 560 + a * 50, y = 200)
        else:
            a = i-114
            letters[chr(i)].place(x = 560 + a * 50, y = 300)
    return 0

def gameProcess():
    ClearScreen()
    secretTales()
    imgPrint()
    alphabetPrint()

def startPress():
    global clicked
    global mistakes
    global rightLets
    mistakes=1
    rightLets=1
    ClearScreen()
    gameProcess()

def StartButPrint():
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

StartButPrint()



if __name__ == "__main__":
	root.mainloop()
        
else:
    word = "test"