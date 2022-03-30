#IDA* search algorithm with multiple hurestic functions
#Alast0r 24 MAY 2022
from queue import PriorityQueue
from graph import *
from itertools import count
unique = count()

class Asearch:
    def __init__(self):
        self.tree = TreeGraph() #The tree excluding leaf/fringe nodes
        self.fringe = PriorityQueue() #Stack for expandable nodes
        self.parent = []
        self.root = None
        self.H = 1

    def getLocation(self,index):
        j = index%3
        if(index > 5):
            i = 2
        elif(index > 2):
            i = 1
        else:
            i = 0
        return i,j

    def swap(self,i,j,seq):
        c = seq[i]
        seq[i] = seq[j]
        seq[j] = c
        return seq

    def getParent(self,node):
        for child,parent in self.parent:
            if child.key == node.key:
                return parent
        return None

    def update(self,seq,cost):
        hf = self.geth(seq)
        node = Node(seq,cost+1)
        #Checking if the node has been visited
        if(self.tree.notIn(node)):
            parent = self.getParent(node)
            #Adding the node to fringe
            if node.key != self.root.key:
                if parent == None:
                    self.fringe.put((node.value+hf,next(unique),node))
                    self.parent.append((node,parent))
                    return
                #Update the vlaue of the cost
                for i in range(len(self.parent)):
                    n,p = self.parent[i]
                    if(n.key == node.key):
                        if(node.value < n.value):
                            self.parent[i] = (node,parent)


    def search(self,STARTSTATE,FINSTATE):
        self.root = Node(STARTSTATE,0)
        self.fringe.put((self.geth(STARTSTATE),next(unique),self.root))

        while not self.fringe.empty():
            node = self.fringe.get()[2]
            seq = node.key.copy()
            cost = node.value

            #Check for termination
            if seq == FINSTATE:
                self.printans(node) 
                return
            #Expanding the tree
            i,j = self.getLocation(seq.index(0))
            index = i*3+j
            ##left
            if j != 0:
                newindex = i*3+(j-1)
                newSeq = self.swap(index,newindex,seq.copy())
                self.update(newSeq,cost)
            ##right
            if j != 2:
                newindex = i*3+(j+1)
                newSeq = self.swap(index,newindex,seq.copy())
                self.update(newSeq,cost)
            ##up
            if i != 0:
                newindex = (i-1)*3+j
                newSeq = self.swap(index,newindex,seq.copy())
                self.update(newSeq,cost)
            ##down
            if i != 2:
                newindex = (i+1)*3+j
                newSeq = self.swap(index,newindex,seq.copy())
                self.update(newSeq,cost)
            self.tree.addNode(node)    

    #Hurestic Functions
    def geth(self,seq):
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

    #Printing the answer
    def printans(self,node):
        print(node.key,"\n",node.value)
        print("Closed List",len(self.tree.nodeList))
        print("Open List: ",self.fringe.qsize())