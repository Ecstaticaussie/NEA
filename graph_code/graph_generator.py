import networkx as nx
from random import randint

def graph_generator():
    #A funciton for creating a graph object
    def myGraphCreate(nodes, edges):
        myGraph = nx.Graph()
        myGraph.add_nodes_from(nodes)
        myGraph.add_edges_from(edges)
        return myGraph

    #initial graph variables
    myGraphBefore = nx.Graph()
    numNodes = randint(8, 13)
    numEdges = randint(numNodes+2, numNodes + 3)
    nodeList = list(range(1, numNodes+1))
    edgeList = []
    #Used to create edges (see further down)
    edgesCreatedPerNode = [randint(2,4) for _ in range(numNodes)]
    midpoint = len(nodeList)//2 - 1

    #This is to act as a limit for the edges
    while len(edgeList) < numEdges:
        for index in range(numNodes):
            if edgesCreatedPerNode[index] > 0:
                #Each element in edgesCreatedPerNode is used an offset to decide what edges it goes to
                #For items beyond the midpoint, you subtract instead of add to the index
                if index > midpoint: currentEdgeNum = edgesCreatedPerNode[index] * -1
                else: currentEdgeNum = edgesCreatedPerNode[index]
                #Randomly decides if an edge is created. No duplicates are stored and the edge is stored in order
                if randint(0, 1):
                    if nodeList[index] < nodeList[index + currentEdgeNum]:
                        edge = (nodeList[index], nodeList[index + currentEdgeNum])
                    else: edge = (nodeList[index+currentEdgeNum], nodeList[index])

                    #Reverses nodeList to increases randomness
                    nodeList = list(reversed(nodeList))
                    if edge not in edgeList:
                        edgeList.append(edge)
                        #Reduces the possible edges with the node by 1
                        edgesCreatedPerNode[index] = edgesCreatedPerNode[index] - 1
    
    #This is used as a before graph to check for changes
    nodeList = sorted(nodeList)
    myGraphBefore.add_nodes_from(nodeList)
    myGraphBefore.add_edges_from(edgeList)

    while True:
        myGraphAfter = myGraphCreate(nodeList, edgeList)
        #Nodes with either 1 or 0 neighbours are removed
        #The graph is then updated
        for node in nodeList:
            if len(list(nx.neighbors(myGraphAfter, node))) == 1:
                #Finds it's neighbour node and removes the edge (orders the nodes)
                neighborNode = list(nx.neighbors(myGraphAfter, node))[0]
                if node < neighborNode: removeEdge = (node, neighborNode)
                else: removeEdge = (neighborNode, node)
                edgeList.remove(removeEdge)
                myGraphAfter = myGraphCreate(nodeList, edgeList)

            if len(list(nx.neighbors(myGraphAfter, node))) == 0:
                nodeList.remove(node)
                myGraphAfter = myGraphCreate(nodeList, edgeList)
            
        #If there are no changes in the graph, the loop is broken
        #If there are changes, myGraphBefore is reassigned such that the loop can continue
        if myGraphBefore.edges == myGraphAfter.edges: break
        myGraphBefore = myGraphAfter

    myGraph = myGraphCreate(nodeList, edgeList)
    return myGraph