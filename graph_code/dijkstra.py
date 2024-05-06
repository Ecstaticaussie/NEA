import networkx as nx
from graph_adjuster import graph_adjuster

"""
This will store info about each step in Dijkstra's
Shows information about the graph at the step's execution in the algorithm
"""
class DijkStep:
    def __init__(self):
        #this will be altered when drawing the graph
        self.colour = None

        #To store working values of nodes
        self.visited_node = None
        self.scores = []

        self.nodes_and_working_values = {}
        self.edges = []

    def store_working_value(self, node, working_value):
        self.nodes_and_working_values[node] = working_value

    def store_visited_node(self, visited_node):
        self.visited_node = visited_node

    def store_edge(self, edge):
        self.edges.append(edge)

"""
This will represent the shortest distance for one node in the graph
Lots of these will be created for the Priority Queue when dijkstra_algorithm() is being executed
"""
class QueuedItem:
    def __init__(self, label, value):
        self.label = label
        self.value = value

"""
We need this data structure to decide which node to visit next in the algorithm
The criteria is that we pick the node which has the shortest distance from the scores dictionary AND the node has not been visited
In this implementation, there will be no set limit for the queue's length
However, due to the way the graphs are generated, there is a limit to the number of nodes in the graph, so there is a limit to the length of the queue
"""
class PriorityQ:
    def __init__(self):
        self.queue = []

    #Allows the queue to be used as an iterable for a for loop
    def __iter__(self):
        for item in self.queue:
            yield item

    def __len__(self):
        return len(self.queue)
    
    #Going through the queue and inserting item_to_queue when it's value is more than an item in the queue at a certein index
    def push(self, label, value):
        item_to_queue = QueuedItem(label, value)
        if len(self.queue) == 0: self.queue.append(item_to_queue)
        else:
            for i in range(len(self.queue)):
                if item_to_queue.value > self.queue[i].value:
                    self.queue.insert(i, item_to_queue)
                    break

                #This is for when all the other scores for the nodes are bigger
                if i == len(self.queue) - 1:
                    self.queue.append(item_to_queue)

    def pop(self, label=None):
        if label:
            for item in self.queue:
                if item.label == label:
                    self.queue.remove(item)

        if len(self.queue) > 0:
            return self.queue.pop()

    def find_label(self, label):
        for item in self.queue:
            if item.label == label:
                return True
        return False

    def get_item_value(self, label):
        for item in self.queue:
            if item.label == label:
                return item.value
    
    def set_item_value(self, label, value):
        for item in self.queue:
            if item.label == label:
                item.value = value

"""
####### The actual dijkstra's algorithm ########

Find all edges that connect to current_node

Update scores(list) using these edges

Add + update nodes in unvisited_nodes_q

Decide current node
"""
class DijkstraAlgo:
    #setting up variables and data structures
    def __init__(self, myGraph, start_node="1"):
        self.myGraph = myGraph
        self.previous_node = {}
        self.is_node_visited = {}
        self.scores = {}
        self.all_nodes_visited = {}

        self.unvisited_nodes_q = PriorityQ()
        self.unvisited_nodes_q.push(start_node, 0)

        self.visited_edges = []

        for node in sorted(self.myGraph.nodes):
            self.previous_node[str(node)] = None
            self.is_node_visited[str(node)] = False
            self.scores[str(node)] = float("inf")
            self.all_nodes_visited[str(node)] = True

        self.scores[start_node] = 0
        self.previous_node[start_node] = None

        self.steps = []

    def get_node_connections(self, node):
        x = [edge for edge in list(self.myGraph.edges) if node in edge]
        #We sort each edge so that it can be used for as a key for a dictionary
        return [tuple(sorted(edge)) for edge in x]

    def execute(self):
        while len(self.unvisited_nodes_q) != 0:
            #Where graph changes are stored for each step
            current_DijkStep = DijkStep()

            node_and_distance = self.unvisited_nodes_q.pop()
            current_node = node_and_distance.label
            current_DijkStep.store_visited_node(current_node)

            score = node_and_distance.value
            self.is_node_visited[current_node] = True
            current_node_connections = self.get_node_connections(current_node)

            for current_edge in current_node_connections:
                if current_edge not in self.visited_edges:
                    self.visited_edges.append(current_edge)
                    current_DijkStep.store_edge(current_edge)
                    connected_node = current_edge[0] if current_edge[0] != current_node else current_edge[1]
                    if self.is_node_visited[connected_node]:
                        continue

                    #We have this try and except as the edges are represented by nodes which are ordered by their direction when created
                    #They don't have a direction, but you can't access edge unless you have the nodes ordered correctly
                    try:
                        current_edge_weight = nx.get_edge_attributes(self.myGraph, "weight")[current_edge]
                    except KeyError:
                        reversed_edge = (current_edge[1], current_edge[0])
                        current_edge_weight = nx.get_edge_attributes(self.myGraph, "weight")[reversed_edge]

                    new_score = score + current_edge_weight
                    if new_score < self.scores[connected_node]:
                        current_DijkStep.store_working_value(connected_node, new_score)
                        self.scores[connected_node] = new_score
                        self.previous_node[connected_node] = current_node
                        self.unvisited_nodes_q.push(connected_node, new_score)

            self.steps.append(current_DijkStep)

    def show_algorithm_end(self):
        print("Scores: ", self.scores)
        print("Previous Nodes: ", self.previous_node)
        print("Nodes Visited: ", self.is_node_visited)

        for step in self.steps:
            print("\n")
            print("Visited node:", step.visited_node)
            print("Visited edges:",step.edges)
            print("Scores:", step.nodes_and_working_values)

myGraph = graph_adjuster(True)[0] #Using only the graph (seen with [0]) as graph_adjuster() returns a tuple of different objects)
myDijkstra = DijkstraAlgo(myGraph, "1")
myDijkstra.execute()
myDijkstra.show_algorithm_end()