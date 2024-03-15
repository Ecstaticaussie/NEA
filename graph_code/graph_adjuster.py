from graph_generator import nodes_edges_generator, myGraphCreate
import networkx as nx

#Where the label of the nodes are changed
def graph_mapper():
    nodeList, edgeList = nodes_edges_generator()
    myGraph = myGraphCreate(nodeList, edgeList)
    #To create the mapping, we need to get node positions from left to right
    node_positions = nx.spring_layout(myGraph)
    for node in node_positions:
        print(node, node_positions[node])

    #return mappedGraph

graph_mapper()