#Iteratice Deeping Search algorithm representation 
#Alast0r 23 MAY 2022
from collections import deque
from itertools import count
from time import sleep
unique = count()
from graph import *

PUZZLE=3

class ids:
    def __init__(self):
        self.tree = TreeGraph() #The search tree for the algorithm
        self.fringe = deque() #Queue for expandable nodes
        self.parent = [] #Each nodes parent(only the ones that are have not been visited twice)
        self.visited = [] #Nodes that are visited
        self.root = None
        self.maxdepth = 0 #max depth of the 
        self.isDone = False #Checks if it can stop iterating
        self.MAX = 10000

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
        return None, None, None #The state has not been seen yetarent
        return None

    #Expanding a node
    def update(self,seq,parent,dir):
        depth = parent.value
        #Adding the node to the search tree
        node = Node(seq,depth+1)
        parent.addChild(node)
        self.tree.addNode(node)
        #Checking the max depth of the tree
        if(depth+1 > self.maxdepth):
                self.maxdepth = depth+1
        #Checking if the state is not visisted:
        if(not seq in self.visited):
            #Checking if the state is inside the queue (has a parent)
            nChild,nParent,dir2 = self.getParent(node)
            if not nParent == None :
                #Getting the pair index
                i = self.parent.index((nChild,nParent,dir2))
                if nChild.value > node.value :
                    self.parent[i] = (node,parent,dir)
                    self.fringe.append(node) 
            self.fringe.append(node)
            self.parent.append((node,parent,dir)) 

    #Main function
    def search(self,STARTSTATE,FINSTATE):
        self.isDone = False
        depth = 0 #Depth iteration number
        #start iterating
        ans = "The depth value exceeded" + str(self.MAX)
        while not self.isDone:
            #reseting everything!
            self.tree = TreeGraph() #The search tree for the algorithm
            self.fringe = deque() #Queue for expandable nodes
            self.parent = [] #Each nodes parent(only the ones that are have not been visited twice)
            self.visited = [] #Nodes that are visited
            self.root = None
            self.maxdepth = 0 #max depth of the
            #start the iteration on depth i 
            ans = self.dfs(STARTSTATE,FINSTATE,depth)
            #Moving to the next iteration
            depth += 1
            if depth == self.MAX:
                break
        return ans

    def dfs(self,STARTSTATE,FINSTATE,MAXDEPTH):
        #Creating the root 
        self.root = Node(STARTSTATE,0) #The value is depth of node & key is the sequence we have
        self.tree.addNode(self.root)
        self.fringe.append(self.root) 
        self.parent.append((self.root,self.root,"[Root]"))
        #Start the serach
        while not len(self.fringe) == 0:
            node = self.fringe.pop() #get the next state
            seq = node.key.copy() #The state of the puzzle
            depth = node.value #The depth of the puzzle
            #check for termination
            if seq == FINSTATE:
                self.isDone = True
                return self.printans(node)
            #iterating for depth
            if depth == MAXDEPTH:
                continue
            #Expanding the tree
            index = seq.index(0)
            i,j = self.getIndex(index) 
            ##left
            if j != 0:
                newindex = i*3+(j-1)
                newSeq = self.swap(index,newindex,seq.copy())
                self.update(newSeq,node,"[Left]")
            ##Right
            if j != 2:
                newindex = i*3+(j+1)
                newSeq = self.swap(index,newindex,seq.copy())
                self.update(newSeq,node,"[Right]")
            ##Up
            if i != 0:
                newindex = (i-1)*3+j
                newSeq = self.swap(index,newindex,seq.copy())
                self.update(newSeq,node,"[Up]")
            ##Down
            if i != 2:
                newindex = (i+1)*3+j
                newSeq = self.swap(index,newindex,seq.copy())
                self.update(newSeq,node,"[Down]")
            #Adding the sequnce to the visited 
            self.visited.append(seq)    
        return None

    #Printing the answer
    def printans(self,node):
        if node == None:
            return "Unfrotunetly no answer was found using this algorithm for this initial state"
        else:
            path = deque()
            cost = str(node.value)   #Cost/depth of the answer
            expanded = str(len(self.visited)) #Number of nodes expanded
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
            ans += "\nCost of the path: " + cost + "\nNumber of nodes-expanded: " + expanded +"\nMaximum depth: " + str(self.maxdepth) 
            return ans
