#Puzzle 8 solver using AI informed and uninformed search algorithm
#This part is the interface that you can use to created the puzzle, chose what algorithm you want to use and shows the resault of said search.
#Arshia Moradi 02 April 2022 

from glob import glob
import re   #Regix 
from random import shuffle #Randomizer
#Tkinter imports
from tkinter import * 
from tkinter import messagebox

import tracemalloc #memmory mesurement
import time #time mesurement 

#Search algorithms
from a import Asearch #A* Search
from ucs import ucs #Uninformed cost search
from ids import ids #Iterative deeping search

window = Tk() #The main  
window.title("AI project by Arshia Moradi")
Label(window,text="Puzzle 8 Solver",font = 'calibri').grid(row=0,column=0,columnspan=2)

puzzleFrame = Frame(window,padx=2,pady=2)   #8 Puzzle show and design
puzzleFrame.grid(row=1,column=0)
initFrame = Frame(window)   #8 Puzzle show and design
initFrame.grid(row=1,column=1)
searchFrame = Frame(window,padx=2)   #Start search and search conditions
searchFrame.grid(row=2,column=0,columnspan=2,sticky='w')
infoFrame = Frame(window,padx=2,pady=5)     #Answer of the search
infoFrame.grid(row=3,column=0,columnspan=2,sticky='w')

#Getting the initial state of the puzzle
def getState():
    STATE = [] 
    for button in puzzle:
        c = button['text']
        if c == "  " : #Finding the white space
            STATE.append(0)
        else:
            STATE.append(int(c))
    return STATE 

#Creating the Puzzle Frame:
seq = ["  ","1","2","3","4","5","6","7","8"]
puzzle = []
for i in range(9):
    button =  Button(puzzleFrame, text = seq[i],borderwidth=2,padx=40,pady=20,bg='#97A6B7',fg = 'black')
    button.grid(row=int(i/3),column=i%3) 
    puzzle.append(button)
    
#Getting a manual input for puzzle
def initInput():
    input = stateE.get()
    #Checkign for valid inputs
    if(not re.search("^([0-8])([,])([0-8])([,])([0-8])([,])([0-8])([,])([0-8])([,])([0-8])([,])([0-8])([,])([0-8])([,])([0-8])$",input)):
        messagebox.showerror("Invalid Type","The input must only consist of 0-8 and has the format like this:\n 0,1,2,3,4,5,6,7,8")
        return False
    #Check if the sequnce is valid or not
    inputSeq = re.split(",",input)
    if len(inputSeq) > len(set(inputSeq)):
        messagebox.showerror("Invalid Input Sequnce","The input most only be a sequnce from 0 to 8 with no two numbers alike. for example:\n 0,1,2,3,4,5,6,7,8")
        return False
    #Changing the puzzles
    for i in range(9):
        if inputSeq[i] == "0" :
            c = "  "
        else:
            c = inputSeq[i]
        puzzle[i].config(text=c)
    return True
#Getting Random input for puzzle    
def initRandom():
    seq = ["  ","1","2","3","4","5","6","7","8"]
    shuffle(seq)
    for i in range(9):
        puzzle[i].config(text = seq[i])

#Creating the initFrame
Label(initFrame,text="Enter custom initial state:",justify=LEFT).pack()
stateE = Entry(initFrame,width=25,borderwidth=5)
stateE.insert(0, "0,1,2,3,4,5,6,7,8")
stateE.pack()
buttonInput = Button(initFrame, text = "Change State", padx=60,pady=20,command=initInput).pack()
buttonRandom = Button(initFrame, text = "Ranzdomized State", padx=45,pady=20,command=initRandom).pack()

#Creating answer frame
Label(infoFrame, text = "The resaluts of the search:", font='-*-lucidatypewriter-medium-r-*-*-*-140-*-*-*-*-*-*',padx=2,pady=5).grid(row=0,column=0,sticky='w')
ansLabel = Label(infoFrame, text = "",wraplengt=475,padx=2,pady=2,justify=LEFT)
ansLabel.grid(row=1,column=0,sticky='w')

#Creating the search frame

#Starting the search
def clickStart():
    INISTATE = getState()
    FINSTATE = [0,1,2,3,4,5,6,7,8]
    #Checking if the puzzle is solvable:
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
    tracemalloc.reset_peak() #find out how much memorry is used
    start_time = time.time() #start mesuring time
    if op == "UCS":
        ans = ucs().search(INISTATE,FINSTATE)
    elif op == "IDS":
        ans = ids().search(INISTATE,FINSTATE)
    elif op == "A*":
        ans = Asearch(hf).search(INISTATE,FINSTATE)
    else:
        messagebox.showinfo("Non Feature","The IDA* search has not been implemented yet in the system.")
        ans = ""
    ans += "Memmory usage: Size " + str(tracemalloc.get_traced_memory()[0]) + "Kib Peak " + str(tracemalloc.get_traced_memory()[1])+ "Kib\n"
    ans += "Time: " + str(time.time()-start_time)
    #Showing the answer       
    ansLabel['text'] = ans

#Serach options - readio buttons
def callback(*args):
    if(opVar.get() == "UCS" or opVar.get() == "IDS"):
        huresticOp.config(state=DISABLED)
    else:
        huresticOp.config(state=NORMAL)

#Creating the searchFrame
buttonStrat = Button(searchFrame, text = "Start", padx=55,pady=10,command=clickStart)
buttonStrat.grid(row = 0)

opVar = StringVar()
opVar.set("UCS")
opVar.trace("w",callback)
searchOp = OptionMenu(searchFrame,opVar,"UCS","IDS","A*","IDA*")
searchOp.grid(row = 0,column = 1, padx=4,pady=2)

#Hurestic Functions
hVar = StringVar()
hVar.set("h1")
huresticOp = OptionMenu(searchFrame,hVar,"h1","h2")
huresticOp.config(state=DISABLED)
huresticOp.grid(row = 0,column = 2, padx=4,pady=2)


#main loop
tracemalloc.start()
window.mainloop()
tracemalloc.stop()