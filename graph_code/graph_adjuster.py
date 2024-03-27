from graph_code.graph_generator import nodes_edges_generator, myGraphCreate
import networkx as nx
from random import randint

#Where the label of the nodes are changed
#This is done left to right
def graph_mapper():
    nodeList, edgeList = nodes_edges_generator()
    myGraph = myGraphCreate(nodeList, edgeList)

    #return myGraph                               #
    #To create the mapping, we need to get node positions from left to right
    #We create a 'key-value pair' of previous node label to new node label (from ordered_nodes) in a zip object
    ordered_nodes = list(range(1, len(nodeList)+1))
    node_positions = nx.spring_layout(myGraph)

    #return_node_positions is a copy of of node_positions
    #I need the same key:value pairs as it changes with each call of nx.springlayout()
    #copy() is not achieving the results i want to
    return_node_positions = {key:node_positions[key] for key in node_positions} 

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

    print(new_mapping)
    return mappedGraph, return_node_positions

def add_weights(myGraph):
    pass