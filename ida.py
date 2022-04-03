#Iteratice Deeping A* Search algorithm representation 
#Alast0r 23 MAY 2022
from collections import deque
from itertools import count
from sre_constants import MAX_UNTIL
from telnetlib import STATUS
unique = count()
from graph import *

PUZZLE=3
MAXINT = 10000000

class IDAsearch:
    def __init__(self,H1=1):
        self.parent = [] #Each nodes parent(only the ones that are have not been visited twice)
        self.expanded = 0 #Nodes that are visited
        self.root = None
        self.finNode = None
        self.maxdepth = 0 #max depth of the 
        self.H = 1 #Huristic function we want to do search with
    
    #Gets the location of the zero/white space in the sequnce        
    def getIndex(self,index):
        j = index%PUZZLE
        i = int(index/PUZZLE)
        return i,j

    #Move the zero/whitespace to new index
    def swap(self,i,j,seq):
        c = seq[i]
        seq[i] = seq[j]
        seq[j] = c
        return seq

    #Checking if a state(not a node) has a parent
    def getParent(self,node):
        for child,parent,dir in self.parent:
            if child.key == node.key :
                return child, parent, dir
        return None, None, None #The state has not been seen yet

    #Hurestic Functions
    def hurestic(self,seq):
        if(self.H==1):
            return self.h1(seq)
        elif(self.H==2):
            return self.h2(seq)    

    def h1(self,seq): #Number of wrong/misplaced numbers
        count = 0
        for i in range(len(seq)):
            if(i != seq[i]):
                count+=1
        return count

    def h2(self,seq): #Manhattan huristic 
        count = 0
        for i in range(len(seq)):
            if not i == seq[i]:
                i1,j1 = self.getLocation(i) #Our current location
                i2,j2 = self.getLocation(seq[i]) #Desired location
                count += abs(i1-i2) + abs(j1-j2)
        return count

    #The search function
    def search(self,INITSTATE,FINSTATE):
        self.root = Node(INITSTATE,0)
        threshhold = self.hurestic(INITSTATE)
        while True:
            self.expanded = 0
            self.maxdepth = 0
            self.parent = []
            self.parent.append((self.root,self.root,"[Root]"))
            cost = self.ids(self.root,FINSTATE,threshhold)
            if cost == MAXINT:
                self.finNode = None
                return self.printans()
            elif cost < 0:
                return self.printans()
            else:
                threshhold = cost

    #Iterative Deeping A* Search
    def ids(self,node,FINSTATE,maxCost):      
        seq = node.key.copy() #Getting the sequnce
        depth = node.value #Getting the depth of node
        #print("Checking node:",seq," Depth:",depth)
        #Checking if the node is the answer
        if seq == FINSTATE:
            self.finNode = node
            return -1
        
        #Checking if we can expand the node
        cost = depth + self.hurestic(seq)
        if cost > maxCost:
            return cost 
        
        #We are expanding this node 
        self.expanded += 1
        if depth + 1 > self.maxdepth:
            self.maxdepth = depth + 1    
                    
        #Getting the index of 0
        index = seq.index(0)
        i,j = self.getIndex(index) 
        min = MAXINT #MAXINT
        #Expand the children
        for x in range(4):
            newSeq = [] #The next state of the puzzle
            dir = "" #The direction we want to go
            hasChild = False
            if x==0 and j != 0: #left
                newindex = i*3+(j-1)
                newSeq = self.swap(index,newindex,seq.copy())
                dir = "[Left]"
                hasChild = True
            if x==1 and j != 2: #Right
                newindex = i*3+(j+1)
                newSeq = self.swap(index,newindex,seq.copy())
                dir = "[Right]"
                hasChild = True
            if x==2 and i != 0: #Up
                newindex = (i-1)*3+j
                newSeq = self.swap(index,newindex,seq.copy())
                dir = "[Up]"
                hasChild = True
            if x==3 and i != 2: #Down
                newindex = (i+1)*3+j
                newSeq = self.swap(index,newindex,seq.copy())
                dir = "[Down]"
                hasChild = True

            if not hasChild: #Skipping if one of the iterations cannot be achived
                continue
            #Creating the node:
            newNode = Node(newSeq,depth+1)
            self.parent.append((newNode,node,dir))
            #Checking what to do
            newCost = self.ids(newNode,FINSTATE,maxCost) #Start search on this node
            if newCost < 0: #NOde was found
                return newCost
            elif newCost < min:
                min = newCost
                
        return min
               
    #Printing the answer
    def printans(self):
        node = self.finNode
        if node == None:
            return "Unfrotunetly no answer was found using this algorithm for this initial state"
        else:
            path = deque()
            cost = str(node.value)   #Cost/depth of the answer
            expanded = str(self.expanded) #Number of nodes expanded
            #Getting the path
            node, parent, dir = self.getParent(node)
            while(node != self.root):
                path.append(dir)
                node = parent
                node, parent, dir = self.getParent(node)
            #Calculating the ansswer
            ans = ""
            while(len(path) > 0):
                ans += path.pop() + "->"
            ans += "Fin"
            ans += "\nCost of the path: " + cost + "\nNumber of nodes-expanded: " + expanded + "\nMaximum depth: " + str(self.maxdepth) 
            return ans
 
I = [1,2,5,0,3,4,6,7,8]
E = [0,1,2,3,4,5,6,7,8]
print(IDAsearch().search(I,E))
