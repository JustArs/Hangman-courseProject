import tkinter as tk
from random import randint
from HangmanTerm import HangmanTerm as ht
from HangmanTerm import secret 

mistakes = 1
r = ht()
newArr = []
for i in range(len(r)) :
    newArr.append("  ?  ")
rightLets = 0

aClicked,bClicked,cClicked,dClicked,eClicked,fClicked,gClicked,hClicked,iClicked,jClicked,kClicked,lClicked,mClicked = (0,)*13
nClicked,oClicked,pClicked,qClicked,rClicked,sClicked,tClicked,uClicked,vClicked,wClicked,xClicked,yClicked,zClicked = (0,)*13

root = tk.Tk()

root.title("Hangman")
root.geometry("1280x720")
root["bg"] = "#ffef9b"
root.resizable(width=True, height=True)

HangTxtImg = tk.PhotoImage(file = "splashscr.png")
Hangimg = tk.Label(root, image=HangTxtImg, bg="#ffef9b")
Hangimg.place(x=330, y=20)

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
    global r
    global newArr
    global rightLets
    if mistakes == 9:
        ClearScreen()
        tk.Label(root, 
                 text = "You lose!", 
                 font="Century 16", 
                 bg="#ffef9b").pack()
        r = ht()
        newArr = []
        for i in range(len(r)) :
            newArr.append("  ?  ")
        StartButPrint()
        imgPrint()
        rightLets = 0
        mistakes = 1

    elif rightLets == len(newArr):
        ClearScreen()
        tk.Label(root, 
                 text = "You win!", 
                 font="Century 16", 
                 bg="#ffef9b").pack()
        r = ht()
        newArr = []
        for i in range(len(r)) :
            newArr.append("  ?  ")
        StartButPrint()
        imgPrint()
        rightLets = 0
        mistakes = 1 
        
def FindLetter(letter, letters):

    global newArr
    global mistakes
    global rightLets
    print("Mistakes = ", mistakes)

    ClearScreen()

    if letter in r:
        print(letter, " - yes!!")
        newArr = secret(letter, newArr, r)
        rightLets += 1
        secretTales()
        alphabetPrint()
        imgPrint()
        print(newArr)
        
    else:
        if mistakes < 9:
            mistakes += 1
        print(letter, " - No!!")
        secretTales()
        alphabetPrint()
        imgPrint()
    checkToWin()

def switchA():
    global aClicked
    aClicked = 1
    Aletter['state'] = tk.DISABLED

def switchB():
    global bClicked
    bClicked = 1
    Bletter['state'] = tk.DISABLED

def switchC():
    global cClicked
    cClicked = 1
    Cletter['state'] = tk.DISABLED

def switchD():
    global dClicked
    dClicked = 1
    Dletter['state'] = tk.DISABLED

def switchE():
    global eClicked
    eClicked = 1
    Eletter['state'] = tk.DISABLED

def switchF():
    global fClicked
    fClicked = 1
    Fletter['state'] = tk.DISABLED

def switchG():
    global gClicked
    gClicked = 1
    Gletter['state'] = tk.DISABLED

def switchH():
    global hClicked
    hClicked = 1
    Hletter['state'] = tk.DISABLED

def switchI():
    global iClicked
    iClicked = 1
    Iletter['state'] = tk.DISABLED

def switchJ():
    global jClicked
    jClicked = 1
    Jletter['state'] = tk.DISABLED

def switchK():
    global kClicked
    kClicked = 1
    Kletter['state'] = tk.DISABLED

def switchL():
    global lClicked
    lClicked = 1
    Lletter['state'] = tk.DISABLED

def switchM():
    global mClicked
    mClicked = 1
    Mletter['state'] = tk.DISABLED

def switchN():
    global nClicked
    nClicked = 1
    Nletter['state'] = tk.DISABLED

def switchO():
    global oClicked
    oClicked = 1
    Oletter['state'] = tk.DISABLED

def switchP():
    global pClicked
    pClicked = 1
    Pletter['state'] = tk.DISABLED

def switchQ():
    global qClicked
    qClicked = 1
    Qletter['state'] = tk.DISABLED

def switchR():
    global rClicked
    rClicked = 1
    Rletter['state'] = tk.DISABLED

def switchS():
    global sClicked
    sClicked = 1
    Sletter['state'] = tk.DISABLED

def switchT():
    global tClicked
    tClicked = 1
    Tletter['state'] = tk.DISABLED

def switchU():
    global uClicked
    uClicked = 1
    Uletter['state'] = tk.DISABLED

def switchV():
    global vClicked
    vClicked = 1
    Vletter['state'] = tk.DISABLED

def switchW():
    global wClicked
    wClicked = 1
    Wletter['state'] = tk.DISABLED

def switchX():
    global xClicked
    xClicked = 1
    Xletter['state'] = tk.DISABLED

def switchY():
    global yClicked
    yClicked = 1
    Yletter['state'] = tk.DISABLED

def switchZ():
    global zClicked
    zClicked = 1
    Zletter['state'] = tk.DISABLED
   
def alphabetPrint():
    global Aletter,Bletter,Cletter,Dletter,Eletter,Fletter,Gletter,Hletter,Iletter,Jletter,Kletter,Lletter,Mletter
    global Nletter,Oletter,Pletter,Qletter,Rletter,Sletter,Tletter,Uletter,Vletter,Wletter,Xletter,Yletter,Zletter

    Aletter = tk.Button(root, text = "A", font="Century 16", command=lambda:[FindLetter("a", ht),switchA()])
    if aClicked == 1:
        Aletter["state"] = tk.DISABLED
    Aletter.place(x=550,y=120)
    Bletter = tk.Button(root, text = "B", font="Century 16", command=lambda:[FindLetter("b", ht),switchB()])
    if bClicked == 1:
        Bletter["state"] = tk.DISABLED
    Bletter.place(x=600,y=120)
    Cletter = tk.Button(root, text = "C", font="Century 16", command=lambda:[FindLetter("c", ht),switchC()])
    if cClicked == 1:
        Cletter["state"] = tk.DISABLED
    Cletter.place(x=650,y=120)
    Dletter = tk.Button(root, text = "D", font="Century 16", command=lambda:[FindLetter("d", ht),switchD()])
    if dClicked == 1:
        Dletter["state"] = tk.DISABLED
    Dletter.place(x=700,y=120)
    Eletter = tk.Button(root, text = "E", font="Century 16", command=lambda:[FindLetter("e", ht),switchE()])
    if eClicked == 1:
        Eletter["state"] = tk.DISABLED
    Eletter.place(x=750,y=120)
    Fletter = tk.Button(root, text = "F", font="Century 16", command=lambda:[FindLetter("f", ht),switchF()])
    if fClicked == 1:
        Fletter["state"] = tk.DISABLED
    Fletter.place(x=800,y=120)
    Gletter = tk.Button(root, text = "G", font="Century 16", command=lambda:[FindLetter("g", ht),switchG()])
    if gClicked == 1:
        Gletter["state"] = tk.DISABLED
    Gletter.place(x=850,y=120)
    Hletter = tk.Button(root, text = "H", font="Century 16", command=lambda:[FindLetter("h", ht),switchH()])
    if hClicked == 1:
        Hletter["state"] = tk.DISABLED
    Hletter.place(x=900,y=120)
    Iletter = tk.Button(root, text = "I", font="Century 16", command=lambda:[FindLetter("i", ht),switchI()])
    if iClicked == 1:
        Iletter["state"] = tk.DISABLED
    Iletter.place(x=950,y=120)
    Jletter = tk.Button(root, text = "J", font="Century 16", command=lambda:[FindLetter("j", ht),switchJ()])
    if jClicked == 1:
        Jletter["state"] = tk.DISABLED
    Jletter.place(x=1000,y=120)
    Kletter = tk.Button(root, text = "K", font="Century 16", command=lambda:[FindLetter("k", ht),switchK()])
    if kClicked == 1:
        Kletter["state"] = tk.DISABLED
    Kletter.place(x=550,y=200)
    Lletter = tk.Button(root, text = "L", font="Century 16", command=lambda:[FindLetter("l", ht),switchL()])
    if lClicked == 1:
        Lletter["state"] = tk.DISABLED
    Lletter.place(x=600,y=200)
    Mletter = tk.Button(root, text = "M", font="Century 16", command=lambda:[FindLetter("m", ht),switchM()])
    if mClicked == 1:
        Mletter["state"] = tk.DISABLED
    Mletter.place(x=650,y=200)
    Nletter = tk.Button(root, text = "N", font="Century 16", command=lambda:[FindLetter("n", ht),switchN()])
    if nClicked == 1:
        Nletter["state"] = tk.DISABLED
    Nletter.place(x=700,y=200)
    Oletter = tk.Button(root, text = "O", font="Century 16", command=lambda:[FindLetter("o", ht),switchO()])
    if oClicked == 1:
        Oletter["state"] = tk.DISABLED
    Oletter.place(x=750,y=200)
    Pletter = tk.Button(root, text = "P", font="Century 16", command=lambda:[FindLetter("p", ht),switchP()])
    if pClicked == 1:
        Pletter["state"] = tk.DISABLED
    Pletter.place(x=800,y=200)
    Qletter = tk.Button(root, text = "Q", font="Century 16", command=lambda:[FindLetter("q", ht),switchQ()])
    if qClicked == 1:
        Qletter["state"] = tk.DISABLED
    Qletter.place(x=850,y=200)
    Rletter = tk.Button(root, text = "R", font="Century 16", command=lambda:[FindLetter("r", ht),switchR()])
    if rClicked == 1:
        Rletter["state"] = tk.DISABLED
    Rletter.place(x=900,y=200)
    Sletter = tk.Button(root, text = "S", font="Century 16", command=lambda:[FindLetter("s", ht),switchS()])
    if sClicked == 1:
        Sletter["state"] = tk.DISABLED
    Sletter.place(x=950,y=200)
    Tletter = tk.Button(root, text = "T", font="Century 16", command=lambda:[FindLetter("t", ht),switchT()])
    if tClicked == 1:
        Tletter["state"] = tk.DISABLED
    Tletter.place(x=1000,y=200)
    Uletter = tk.Button(root, text = "U", font="Century 16", command=lambda:[FindLetter("u", ht),switchU()])
    if uClicked == 1:
        Uletter["state"] = tk.DISABLED
    Uletter.place(x=650,y=300)
    Vletter = tk.Button(root, text = "V", font="Century 16", command=lambda:[FindLetter("v", ht),switchV()])
    if vClicked == 1:
        Vletter["state"] = tk.DISABLED
    Vletter.place(x=700,y=300)
    Wletter = tk.Button(root, text = "W", font="Century 16", command=lambda:[FindLetter("w", ht),switchW()])
    if wClicked == 1:
        Wletter["state"] = tk.DISABLED
    Wletter.place(x=750,y=300)
    Xletter = tk.Button(root, text = "X", font="Century 16", command=lambda:[FindLetter("x", ht),switchX()])
    if xClicked == 1:
        Xletter["state"] = tk.DISABLED
    Xletter.place(x=800,y=300)
    Yletter = tk.Button(root, text = "Y", font="Century 16", command=lambda:[FindLetter("y", ht),switchY()])
    if yClicked == 1:
        Yletter["state"] = tk.DISABLED
    Yletter.place(x=850,y=300)
    Zletter = tk.Button(root, text = "Z", font="Century 16", command=lambda:[FindLetter("z", ht),switchZ()])
    if zClicked == 1:
        Zletter["state"] = tk.DISABLED
    Zletter.place(x=900,y=300)


def gameProcess():
    ClearScreen()
    secretTales()
    imgPrint()
    alphabetPrint()

def startPress():
    global aClicked,bClicked,cClicked,dClicked,eClicked,fClicked,gClicked,hClicked,iClicked,jClicked,kClicked,lClicked,mClicked
    global nClicked,oClicked,pClicked,qClicked,rClicked,sClicked,tClicked,uClicked,vClicked,wClicked,xClicked,yClicked,zClicked
    global mistakes
    aClicked,bClicked,cClicked,dClicked,eClicked,fClicked,gClicked,hClicked,iClicked,jClicked,kClicked,lClicked,mClicked = (0,)*13
    nClicked,oClicked,pClicked,qClicked,rClicked,sClicked,tClicked,uClicked,vClicked,wClicked,xClicked,yClicked,zClicked = (0,)*13
    mistakes=1
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

root.mainloop()