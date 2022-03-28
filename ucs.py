#Uniformed Cost Search algorithm representation using graphs.
# #Alast0r 23 MAY 2022
from queue import Queue
from graph import *

class ucs:
    def __init__(self):
        self.tree = TreeGraph() #The tree excluding leaf/fringe nodes
        self.fringe = Queue() #Queue for expandable nodes
        self.parent = []
        self.root = None

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
                    self.fringe.put(node)
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


    def search(self,STARTSTATE,FINSATATE):
        #Starting the search tree
        self.root = Node(STARTSTATE,0)
        self.fringe.put(self.root)
       # self.parent.append((self.root, self.root))
        while not self.fringe.empty():
            node = self.fringe.get()
            seq = node.key.copy()
            depth = node.value
            
            #Check for termination
            if seq == FINSATATE:
                self.printans(node)
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
        print("NO ANSWER FOUND!")

    #Printing the answer
    def printans(self,node):
        print(node.key,"\n",node.value)
        print("Closed List",len(self.tree.nodeList))
        print("Open List: ",self.fringe.qsize())

if __name__ == '__main__':
    START = [1,2,5,0,3,4,6,7,8]
    FIN = [0,1,2,3,4,5,6,7,8]
    ucs().search(START,FIN)