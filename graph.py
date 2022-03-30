#A representation for graphs and trees used in the project
#Alast0r 27/MAR/2022

#Each node or vertex of the graph
class Node:
    def __init__(self,key,value=None):
        self.key = key #Node identifire
        if(value != None):
            self.value = value
        else:
            self.value = None
        self.children = [] #List of adjacent node
        self.visited = False
    
    #Adding a edge to the node
    def addChild(self,node,edge=1):
        self.children.append((node,edge)) #adds the child and corrisponded edge wieght (default is 1)
        return node

    #Getting the wight of an edge
    def getEdge(self,node):
        for child,edge in self.children:
            if(child == node):
                return edge 
        return None #if the edge doesn't exists

#A Tree Graph representation using Nodes
class TreeGraph:
    def __init__(self):
        self.nodeList = [] #All vertecies in the graph
        
    #Check if a specific key is inside the graph is inside the graph
    def notIn(self,node):
        for nodes in self.nodeList:
            if(nodes.key == node.key):
                return False #The node is inside the graph
        return True

    #Adding a node to the 
    def addNode(self,node):
        self.nodeList.append(node)
    
        
    #Utility function
    def print(self):
        for node in self.nodeList:
            print("Node:",node.key)
            print("Children List:")
            for child, edge in node.children:
                print(edge," -> ",child.value)


