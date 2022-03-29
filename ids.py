#Iteratice Deeping Search algorithm representation 
# #Alast0r 23 MAY 2022
from collections import deque
from graph import *


class ids:
    def __init__(self):
        self.tree = TreeGraph() #The tree excluding leaf/fringe nodes
        self.fringe = deque() #Stack for expandable nodes
        self.parent = []
        self.root = None
        self.checksum = 0
        self.MAXITERATION = 100000

    def getParent(self,node):
        for child,parent in self.parent:
            if child.key == node.key:
                return parent
        return None

    #Expanding a node
    def update(self,seq,cost):
        node = Node(seq,cost+1)
        #Checking if the node has been visited
        if(self.tree.notIn(node)):
            parent = self.getParent(node)
            #Adding the node to fringe
            if node.key != self.root.key :
                if parent == None:
                    self.fringe.append(node)
                    self.parent.append((node,parent))
                    return
                #update the value of the cost
                for i in range(len(self.parent)):
                    n,p = self.parent[i]
                    if(n.key == node.key):
                        if(node.value < n.value):
                            self.parent[i] = (node,parent)
    def getZero(self,seq):
        index = seq.index(0)
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

    #Main function
    def search(self,STARTSTATE,FINSTATE):
        #Iterating for depth
        self.checksum = 0
        for i in range(self.MAXITERATION):
            #Resetting everything:
            self.tree = TreeGraph() #The tree excluding leaf/fringe nodes
            self.fringe = deque() #Stack for expandable nodes
            self.parent = []
            self.root = None
            #print("depth :", i)
            #Begin Search
            self.dfs(STARTSTATE,FINSTATE,i)
            if(self.checksum == 1):
                return
        print("NO VALID ANSWERS")

    def dfs(self,STARTSTATE,FINSTATE,MAXDEPTH):
        #starting the serach tree
        self.root = Node(STARTSTATE,0)
        self.fringe.append(self.root)

        while not len(self.fringe) == 0:
            node = self.fringe.pop()
            seq = node.key.copy()
            depth = node.value
            #print("state: ",seq)
            #iterating for depth
            if depth > MAXDEPTH:
                continue
            #check for termination
            if seq == FINSTATE:
                self.printans(node)
                self.checksum = 1
                return
            #Expanding the tree
            i,j = self.getZero(seq)
            index = i*3+j
            ##left
            if j != 0:
                newindex = i*3+(j-1)
                newSeq = self.swap(index,newindex,seq.copy())
                self.update(newSeq,depth)
            ##right
            if j != 2:
                newindex = i*3+(j+1)
                newSeq = self.swap(index,newindex,seq.copy())
                self.update(newSeq,depth)
            ##up
            if i != 0:
                newindex = (i-1)*3+j
                newSeq = self.swap(index,newindex,seq.copy())
                self.update(newSeq,depth)
            ##down
            if i != 2:
                newindex = (i+1)*3+j
                newSeq = self.swap(index,newindex,seq.copy())
                self.update(newSeq,depth)
            self.tree.addNode(node)    


    #Printing the answer
    def printans(self,node):
        print(node.key,"\n",node.value)
        print("Closed List",len(self.tree.nodeList))
        print("Open List: ",len(self.fringe))


if __name__ == '__main__':
    START = [3,1,2,4,5,0,6,7,8]
    FIN = [0,1,2,3,4,5,6,7,8]
    ids().search(START,FIN)