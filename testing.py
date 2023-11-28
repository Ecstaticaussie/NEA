import networkx as nx
import matplotlib.pyplot as plt


graph1 = nx.Graph()
graph1.add_nodes_from([1, 2, 3])

graph1.add_edges_from([(1, 2), (1, 3)])


nx.draw(graph1, with_labels="True", font_weight="bold")
subax1 = plt.subplot(121)

plt.draw()