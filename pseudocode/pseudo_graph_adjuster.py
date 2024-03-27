"""
function graph_mapper():
    nodeList, edgeList = nodes_edges_generator()
    myGraph = myGraphCreate(nodeList, edgeList)

    ordered_nodes = create_nodeList(len(nodeList))
    node_positions = get_positions(myGraph)
    left_to_right_nodes = []

    while len(node_positions) > 0:
        left_most_node = node B (last item in nodeList)
        for i in range(from 0 to len(node_positions)-1):
            if node A's x-coordinate < node B's x-coordinate:
                left_most_node = node A

        left_to_right_nodes.append(left_most_node)
        nodeList.remove(left_most_node)
        delete left_most_node from node_positions

    new_mapping = {
        key: item from left_to_right_nodes
        value: item from ordered_nodes
        from 0 to len(ordered_nodes)
    }
    mappedGraph = relabel_nodes()
    node_positions = get_positions(mappedGraph)

    return mappedGraph, node_posiitons
end function
"""