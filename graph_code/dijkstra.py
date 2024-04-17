from graph_adjuster import graph_adjuster

#This will represent the shortest distance for one node in the graph
#Lots of these will be created for the Priority Queue when dijkstra_algorithm() is being executed
class QueuedItem:
    def __init__(self, label, value):
        self.label = label
        self.value = value

#We need this data structure to decide which node to visit next in the algorithm
#The criteria is that we pick the node which has the shortest distance from the distances dictionary AND the node has not been visited
#In this implementation, there will be no set limit for the queue's length
#However, due to the way the graphs are generated, there is a limit to the number of nodes in the graph, so there is a limit to the length of the queue
class PriorityQueue:
    def __init__(self):
        self.queue = []
    
    ### IMPLEMENT SORTING VIA PRIORITY WHEN PUSHING INTO THE QUEUE ###
    #use a for loop to go through the queue and append the item when it's value is in between 2 items (other criteria apply)
    def push(self, label, value):
        item = QueuedItem(label, value)
        self.queue.append(item)
    
    def pop(self):
        if len(self.queue) > 0:
            return self.queue[-1]



#The actual dijkstra's algorithm
####### SUBJECT TO CHANGE ########
def dijkstra_algorithm(myGraph, start_node="1"):
    previous_node = {}
    is_node_visited = {}
    distances = {}
    for node in sorted(myGraph.nodes):
        previous_node[str(node)] = None
        is_node_visited[str(node)] = False
        distances[str(node)] = float("inf")

    distances[start_node] = 0



#Wanting to use only the graph as graph_adjuster() returns a tuple of different objects
myGraph = graph_adjuster()[0]
dijkstra_algorithm(myGraph)