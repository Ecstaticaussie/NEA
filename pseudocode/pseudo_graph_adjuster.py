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

function add_weights(myGraph):
    weighted_graph = create_blank_graph()
    nodes = get_nodes(myGraph)
    edges = get_edges(myGraph)
    match random number from 1 to 3 (inclusive):
        case 1:
            lower_bound = 1
            upper_bound = 20
        case 2:
            lower_bound = 21
            upper_bound = 99
        case 3:
            lower_bound = 100
            upper_bound = 150

    end match-case
    Add nodes to weighted_graph
    Add weighted edges to weighted_graph with weights

    get_edge_weight_labels(weighted_graph)

    return edge_weigths, weighted_graph
end function

fucntion stringify_nodes(myGraph):
    create an empty graph
    for every node in myGraph:
        cast the node from integer to string
        add this node to the empty graph
    
    for every edge in myGraph:
        add edge to new graph (now it has nodes)

    return new graph
end

function add_empty_vertex_boxes(myGraph):
    create an empty graph
    for every node in myGraph:
            add node to empty graph with the following attributes:
                - node_label
                - order_of_labelling
                - final_label
                - working_values
    
    for every edge
""" 