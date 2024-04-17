from graph_generator import nodes_edges_generator, myGraphCreate
import networkx as nx
from random import randint

#Where the label of the nodes are changed
#This is done left to right
def graph_mapper():
    nodeList, edgeList = nodes_edges_generator()
    myGraph = myGraphCreate(nodeList, edgeList)

    #return myGraph, nx.spring_layout(myGraph)                               #
    #To create the mapping, we need to get node positions from left to right
    #We create a 'key-value pair' of previous node label to new node label (from ordered_nodes) in a zip object
    ordered_nodes = list(range(1, len(nodeList)+1))
    node_positions = nx.spring_layout(myGraph)

    #This will have the nodes ordered from the least to the greatest x-coordinate
    left_to_right_nodes = []

    while len(nodeList) > 0:
        left_most_node = nodeList[-1] #the node with the largest numerical label in nodeList
        for i in range(len(nodeList)-1):
            if node_positions[nodeList[i]][0] < node_positions[left_most_node][0]:
                left_most_node = nodeList[i]

        #Update variables to remove the left_most_node
        left_to_right_nodes.append(left_most_node)
        nodeList.remove(left_most_node)
        del node_positions[left_most_node]

    #Create a new graph with this mapping
    new_mapping = {left_to_right_nodes[i]: ordered_nodes[i] for i in range(len(ordered_nodes))}
    mappedGraph = nx.relabel_nodes(myGraph, new_mapping, copy=True)
    new_node_positions = nx.spring_layout(mappedGraph)

    return mappedGraph, new_node_positions

def add_weights(myGraph):
    weighted_myGraph = nx.Graph()
    nodes = list(myGraph.nodes)
    edges = list(myGraph.edges)
    #Here, I pick one of 3 ranges of random weights for the edges
    match randint(1, 3):
        case 1:
            lower_bound = 1
            upper_bound = 20
        case 2:
            lower_bound = 21
            upper_bound = 99
        case 3:
            lower_bound = 100
            upper_bound = 150

    #Then, we randomly assign the weights to each of the edges
    for node in nodes: weighted_myGraph.add_node(node)
    for edge in edges:
        weighted_myGraph.add_edge(*edge, weight=randint(lower_bound, upper_bound))

    edge_weights = nx.get_edge_attributes(weighted_myGraph, "weight")

    return weighted_myGraph, edge_weights



def graph_adjuster():
    myGraph, node_positions = graph_mapper()
    weighted_myGraph, edge_weights = add_weights(myGraph)
    return weighted_myGraph, node_positions, edge_weights