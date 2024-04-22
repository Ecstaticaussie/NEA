"""
function dijkstra_algorithm(myGraph, start_node):
    set score and previous node of start node
    set all other nodes to  high score to simulate infinity
    repeat until all the nodes are visited
        find unvisited node with lowest score
        for all edges of lowest node - that aren't already visited
            new score = edge weight + score of current node
            if new score < score of node being explored
        append score to score list
        append current node to previous node list for node being explored
    mark current node as visited
end function
"""