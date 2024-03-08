from graph_generator import nodes_edges_generator, myGraphCreate
import networkx as nx

#Where the label of the nodes are changed
def graph_mapper():
    nodeList, edgeList = nodes_edges_generator()
    myGraph = myGraphCreate(nodeList, edgeList)
    """
    LOOK AT DEBUGGING THE MAPPING
    """
    graph_mapping = {str(nodeList[i-1]):str(i) for i in range(1, len(nodeList)+1)}
    mappedGraph = nx.relabel_nodes(myGraph, graph_mapping)
    return mappedGraph