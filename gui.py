#This is a basic GUI setup for getting input for the Puzzle
#Alast0r 22 March 2022
from random import shuffle
import re
from tkinter import *
from tkinter import messagebox
from a import Asearch #A* Search
from ucs import ucs #Uninformed cost search
from ids import ids #Iterative deeping search

root = Tk()
root.title("8 Puzzle Solver")

#Top side label of info
#infoLabel = Label(root, text = "Puzzle initial state",width=35, borderwidth=5)
#infoLabel.grid(row = 0,column=0, columnspan=3, padx=10,pady=10)

#Label for answer
ansText = Label(root, text = "Search Resault:")
ansText.grid(row = 4,column=0, padx=5,pady=5)
ansLabel = Label(root, text = "",justify=LEFT)
ansLabel.grid(row = 5,column=0,columnspan=5,padx=5,pady=5,sticky=W)

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

#Randomizing the input sequnce
def initRandom():
    seq = ["  ","1","2","3","4","5","6","7","8"]
    shuffle(seq)
    for i in range(9):
        c = seq[i]
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

#Starting the search
def clickStart(): 
    INISTATE = []
    FINSTATE = [0,1,2,3,4,5,6,7,8]
    #Getting the initial state
    if(button_0['text'] == "  "):
        INISTATE.append(0)
    else:
        INISTATE.append(int(button_0['text']))
    if(button_1['text'] == "  "):
        INISTATE.append(0)
    else:
        INISTATE.append(int(button_1['text']))
    if(button_2['text'] == "  "):
        INISTATE.append(0)
    else:
        INISTATE.append(int(button_2['text']))
    if(button_3['text'] == "  "):
        INISTATE.append(0)
    else:
        INISTATE.append(int(button_3['text']))
    if(button_4['text'] == "  "):
        INISTATE.append(0)
    else:
        INISTATE.append(int(button_4['text']))
    if(button_5['text'] == "  "):
        INISTATE.append(0)
    else:
        INISTATE.append(int(button_5['text']))
    if(button_6['text'] == "  "):
        INISTATE.append(0)
    else:
        INISTATE.append(int(button_6['text']))
    if(button_7['text'] == "  "):
        INISTATE.append(0)
    else:
        INISTATE.append(int(button_7['text']))
    if(button_8['text'] == "  "):
        INISTATE.append(0)
    else:
        INISTATE.append(int(button_8['text']))
    #Check if puzzle 8 is solvable:
        inv_count = 0 #if inversions are odd then puzzle is not solvable
        for i in range(len(INISTATE)):
            for j in range(i+1,len(INISTATE)):
                if INISTATE[i] != 0 and INISTATE[j] != 0 and INISTATE[i] > INISTATE[j] :
                    inv_count += 1
        if(not inv_count%2 == 0):
            messagebox.showinfo("Not solvable","The puzzle 8 with this initial state cannot be solved. Please try other combinations")
            return

    #Starting the search
    op = opVar.get() #Getting what operation we have
    hf = int(hVar.get()[1]) #Getting the Hurestic function value
    ans = "" #Answer to the serach inlduing all the info we must show
    if op == "UCS":
        ans = ucs().search(INISTATE,FINSTATE)
    elif op == "IDS":
        ans = ids().search(INISTATE,FINSTATE)
    elif op == "A*":
        ans = Asearch(hf).search(INISTATE,FINSTATE)
    else:
        messagebox.showinfo("Non Feature","The IDA* search has not been implemented yet in the system.")
        ans = ""
    #Showing the answer       
    ansLabel.config(text = ans) 
        

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
buttonRandom = Button(root, text = "Ranzdomize", padx=55,pady=20,command=initRandom)
buttonStrat = Button(root, text = "Start", padx=75,pady=10,command=clickStart)

#put buttins on the screen

button_0.grid(row=0 ,column=0)
button_1.grid(row=0 ,column=1)
button_2.grid(row=0 ,column=2)
button_3.grid(row=1 ,column=0)
button_4.grid(row=1 ,column=1)
button_5.grid(row=1 ,column=2)
button_6.grid(row=2 ,column=0)
button_7.grid(row=2 ,column=1)
button_8.grid(row=2 ,column=2)


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
searchOp.grid(row = 3, column = 0, columnspan=1,padx=4,pady=5)

#Hurestic Functions
hVar = StringVar()
hVar.set("h1")
huresticOp = OptionMenu(root,hVar,"h1","h2")
huresticOp.config(state=DISABLED)
huresticOp.grid(row = 3, column = 1,columnspan=1,padx=4,pady=5)

#main loop
root.mainloop()
