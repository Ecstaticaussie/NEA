from graph_generator import myGraphCreate, nodes_edges_generator
import networkx as nx

nodeList, edgeList = nodes_edges_generator()
myGraph = myGraphCreate(nodeList, edgeList)
pos = nx.spring_layout(myGraph)
