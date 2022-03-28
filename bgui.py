#This is a basic GUI setup for getting input for the Puzzle
#Alast0r 22 March 2022
from email import message
from tkinter import *
import re
from tkinter import messagebox

root = Tk()
root.title("8 Puzzle Solver")

#Top side label of info
infoLabel = Label(root, text = "Puzzle initial state",width=35, borderwidth=5)
infoLabel.grid(row = 0,column=0, columnspan=3, padx=10,pady=10)

#Initial State Entry
stateE = Entry(root, width = 25, borderwidth=5)
stateE.insert(0, "0,1,2,3,4,5,6,7,8")
stateE.grid(row=1,column=4,columnspan=3,padx=10,pady=5)

#Initial input for puzzle
def initInput():
    inputSt = stateE.get()
    #Check for valid input format
    if(not re.search("^([0-8])([,])([0-8])([,])([0-8])([,])([0-8])([,])([0-8])([,])([0-8])([,])([0-8])([,])([0-8])([,])([0-8])$",inputSt)):
        messagebox.showerror("Invalid Type","The input most only consist of 0-8 and has the format like this:\n 0,1,2,3,4,5,6,7,8")
        return False
    #Check if the sequnce is valid!
    inputSeq = re.split(",",inputSt)
    if len(inputSeq) > len(set(inputSeq)):
        messagebox.showerror("Invalid Input Sequnce","The input most only be a sequnce from 0 to 8 with no two numbers alike. for example:\n 0,1,2,3,4,5,6,7,8")
        return False
    else:
        for i in range(9):
            #getting the location of the empty space
            c = inputSeq[i]
            if(c == "0"):
                c = "  "
            #checking wich button to update
            if(i == 0):
                button_0.config(text=c)
            if(i == 1):
                button_1.config(text=c)
            if(i == 2):
                button_2.config(text=c)
            if(i == 3):
                button_3.config(text=c)
            if(i == 4):
                button_4.config(text=c)
            if(i == 5):
                button_5.config(text=c)
            if(i == 6):
                button_6.config(text=c)
            if(i == 7):
                button_7.config(text=c)
            if(i == 8):
                button_8.config(text=c)
    return True

button_0 = Button(root, text = "  ", padx=40,pady=20)
button_1 = Button(root, text = "1", padx=40,pady=20) #command=myCommand()
button_2 = Button(root, text = "2", padx=40,pady=20)
button_3 = Button(root, text = "3", padx=40,pady=20)
button_4 = Button(root, text = "4", padx=40,pady=20)
button_5 = Button(root, text = "5", padx=40,pady=20)
button_6 = Button(root, text = "6", padx=40,pady=20)
button_7 = Button(root, text = "7", padx=40,pady=20)
button_8 = Button(root, text = "8", padx=40,pady=20)

buttonInput = Button(root, text = "Initial Sate", padx=60,pady=20,command=initInput)
buttonRandom = Button(root, text = "Ranzdomize", padx=55,pady=20)
buttonStrat = Button(root, text = "Start", padx=75,pady=10)

#put buttins on the screen

button_0.grid(row=1 ,column=0)
button_1.grid(row=1 ,column=1)
button_2.grid(row=1 ,column=2)
button_3.grid(row=2 ,column=0)
button_4.grid(row=2 ,column=1)
button_5.grid(row=2 ,column=2)
button_6.grid(row=3 ,column=0)
button_7.grid(row=3 ,column=1)
button_8.grid(row=3 ,column=2)


buttonInput.grid(columnspan=2,row=0,column=3)
buttonRandom.grid(columnspan=2,row=2,column=3)
buttonStrat.grid(columnspan=2,row=3,column=3)
#Serach options - readio buttons
def callback(*args):
    if(opVar.get() == "UCS" or opVar.get() == "IDS"):
        huresticOp.config(state=DISABLED)
    else:
        huresticOp.config(state=NORMAL)

opVar = StringVar()
opVar.set("UCS")
opVar.trace("w",callback)
searchOp = OptionMenu(root,opVar,"UCS","IDS","A*","IDA*")
searchOp.grid(columnspan=2,padx=4,pady=5)

#Hurestic Functions
hVar = StringVar()
hVar.set("h1")
huresticOp = OptionMenu(root,hVar,"h1","h2")
huresticOp.config(state=DISABLED)
huresticOp.grid(columnspan=2,padx=4,pady=5)

#main loop
root.mainloop()
