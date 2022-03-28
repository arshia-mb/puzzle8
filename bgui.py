#This is a basic GUI setup for getting input for the Puzzle
#Alast0r 22 March 2022
from tkinter import *
from traceback import print_tb

root = Tk()
root.title("8 Puzzle Solver")

#Top side label of info
infoLabel = Label(root, text = "Puzzle initial state",width=35, borderwidth=5)
infoLabel.grid(row = 0,column=0, columnspan=3, padx=10,pady=10)

#Answer Labels
#answerE = Entry(root, width = 35, borderwidth=5, state=DISABLED)
#answerE.grid(row=4,column=0,columnspan=3,padx=1,pady=1)

#Define buttons
def myClick():
    pass

button_1 = Button(root, text = "1", padx=40,pady=20) #command=myCommand()
button_2 = Button(root, text = "2", padx=40,pady=20)
button_3 = Button(root, text = "3", padx=40,pady=20)
button_4 = Button(root, text = "4", padx=40,pady=20)
button_5 = Button(root, text = "5", padx=40,pady=20)
button_6 = Button(root, text = "6", padx=40,pady=20)
button_7 = Button(root, text = "7", padx=40,pady=20)
button_8 = Button(root, text = "8", padx=40,pady=20)
button_9 = Button(root, text = "  ", padx=40,pady=20)

buttonInput = Button(root, text = "Initial Sate", padx=60,pady=20)
buttonRandom = Button(root, text = "Ranzdomize", padx=55,pady=20)
buttonStrat = Button(root, text = "Start", padx=75,pady=10)

#put buttins on the screen

button_1.grid(row=1 ,column=0)
button_2.grid(row=1 ,column=1)
button_3.grid(row=1 ,column=2)
button_4.grid(row=2 ,column=0)
button_5.grid(row=2 ,column=1)
button_6.grid(row=2 ,column=2)
button_7.grid(row=3 ,column=0)
button_8.grid(row=3 ,column=1)
button_9.grid(row=3 ,column=2)

buttonInput.grid(columnspan=2,row=1,column=3)
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
