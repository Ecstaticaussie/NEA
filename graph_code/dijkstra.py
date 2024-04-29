import networkx as nx
from graph_adjuster import graph_adjuster

"""
This will store info about each step in Dijkstra's
This will information about the graph at the step's execution in the algorithm
"""
class DijkStep:
    def __init__(self, id):
        self.id = id

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

        self.further_set_up()

    def further_set_up(self):
        for node in sorted(self.myGraph.nodes):
            self.previous_node[str(node)] = None
            self.is_node_visited[str(node)] = False
            self.scores[str(node)] = float("inf")
            self.all_nodes_visited[str(node)] = True

        self.scores[self.start_node] = 0
        self.previous_node[self.start_node] = None

    #Used as the condition for the while loop in self.execute()
    def are_all_nodes_visited(self):
        if self.all_nodes_visited == self.is_node_visited: return True
        return False

    def get_node_connections(self, node):
        x = [edge for edge in list(self.myGraph.edges) if node in edge]
        #We sort each edge so that it can be used for as a key for a dictionary
        return [tuple(sorted(edge)) for edge in x]

    def update_lists(self):
        self.current_node_neighbours = nx.all_neighbors(self.myGraph, self.current_node)
        for edge in self.current_node_connections:
            #This is to decide what current_node is connected to
            node = edge[0] if edge[0] != self.current_node else edge[1]

            #We have this try and except as the edges are represented by nodes which are ordered by their direction when created
            #They don't have a direction, but you can't access edges unless you have the nodes ordered correctly
            try:
                current_edge_weight = nx.get_edge_attributes(self.myGraph, "weight")[edge]
            except KeyError:
                reversed_edge = (edge[1], edge[0])
                current_edge_weight = nx.get_edge_attributes(self.myGraph, "weight")[reversed_edge]

            current_score = current_edge_weight + self.scores[self.current_node]

            #Updating the score
            if current_score > self.scores[node] or self.scores[node] == float("inf"):
                self.scores[node] = current_score
                self.previous_node[node] = self.current_node

    def update_q(self):
        # Add + update nodes with a lower score
        for node in self.current_node_neighbours:
            if self.is_node_visited[node] == False:
                node_score = self.scores[node]
                if self.unvisited_nodes_q.find_label(node) == False:
                    self.unvisited_nodes_q.push(node, node_score)
                
                #If the new score is less than the one in unvisited_node_q, change it
                elif self.unvisited_nodes_q.get_item_value(node) > node_score:
                    self.unvisited_nodes_q.set_item_value(node, node_score)

        #Remove visited nodes
        for item in self.unvisited_nodes_q:
            if self.is_node_visited[item.label] == True:
                self.unvisited_nodes_q.pop(item.label)
    
    def change_current_node(self):
        self.is_node_visited[self.current_node] = True
        self.current_node = self.unvisited_nodes_q.pop()


    #Where the actual execution occurs
    def execute(self):
        while not self.are_all_nodes_visited():
            self.update_lists()
            self.update_q()
            self.change_current_node()

        print(self.is_node_visited)
        print(self.scores)
        print(self.previous_node)

    def test(self):
        while len(self.unvisited_nodes_q) != 0:
            node_and_distance = self.unvisited_nodes_q.pop()
            self.current_node = node_and_distance.label
            distance = node_and_distance.value
            self.is_node_visited[self.current_node] = True
            self.current_node_connections = self.get_node_connections(self.current_node)
            self.current_node_neighbours = nx.all_neighbors(self.myGraph, self.current_node)
            for current_edge in self.current_node_connections:
                connected_node = current_edge[0] if current_edge[0] != self.current_node else current_edge[1]
                if self.is_node_visited[connected_node]:
                    continue
                edge_weight = nx.get_edge_attributes(self.myGraph, "weight")[current_edge]
                new_distance = distance + edge_weight

myGraph = graph_adjuster(True)[0] #Using only the graph (seen with [0]) as graph_adjuster() returns a tuple of different objects
myDijkstra = DijkstraAlgo(myGraph, "1")
myDijkstra.test()