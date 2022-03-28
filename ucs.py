#This algorithm gets a graph as input and returns the desired output based on ucs algorithm
#Alast0r 23 MAY 2022
from queue import Queue
from graph import *

FINSTATE = [0,1,2,3,4,5,6,7,8]

def check(pList,node):
    for child, parent in pList:
        if child.key == node.key:
            return child
    return None

def getZeor(l):
    x = l.index(0)
    i = x%3

#UCS function based on the input state and the location of the white space
def ucs(inputsq):
    start = Node(inputsq,0) #key is the sequnce and the value is the nodes depth!
    fringe = Queue() #input queue for all expandible nodes
    fringe.put((start,0))
    parent = []  #List of the each nodes parent node (for backtracking the answer)
    parent.append((start,0))
    while not fringe.empty():
        node, cost = fringe.get()
        seq = node.key #The state of the puzzle
        if seq == FINSTATE:
            i,j = getZero(node.key)
    return



if __name__ == '__main__':
    ucs([0,1,2,3,4,5,6,7,8])