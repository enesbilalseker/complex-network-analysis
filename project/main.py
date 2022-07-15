import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

#G = nx.Graph()
# DG = nx.DiGraph()  # directed graph
#H = nx.path_graph(10)

"""
G.add_node(0)  # 0->name of the node can be "a"
G.add_nodes_from([1, 2])
G.add_nodes_from([
    (3, {"color": "red"}),  # nodes can have attributes
    (4, {"color": "green"}),
])
print(G)

G2 = nx.Graph()
H = nx.path_graph(10)  # create 10 node graph, also has 9 edges
print(H)
G2.add_nodes_from(H)
print(G2)
"""

"""
G.add_edge(1, 2)
G.add_edges_from([(1, 2), (1, 3)]) # (source, target)
H = nx.path_graph(10)
G.add_edges_from(H.edges)
print(G.number_of_edges())
print(G.number_of_nodes())
print(G)
# G.clear()
"""

"""
DG.add_edge(2, 1)  # (source, target)
DG.add_edge(1, 3)
DG.add_edge(2, 4)
DG.add_edge(1, 2)

# neighbour nodes for node 2, which nodes can node 2 reach?
print(list(DG.successors(2)))
# neighbour nodes for node 2, nodes that leads to node 2
print(list(DG.predecessors(2)))

print(list(H.neighbors(0)))

H.remove_node(2)
print(H)

print(DG.out_degree(2))
print(DG.in_degree(2))
print(H.degree(1))
"""
"""
GND = nx.to_directed(H)  # GND=Graph Not Directed
GD2 = nx.to_undirected(GND)
print(GND)
print(GD2)
"""

CG = nx.complete_graph(5)  # CG = Complete Graph
halter = nx.barbell_graph(10, 2)
lolipop = nx.lollipop_graph(10, 2)
randomGraph = nx.erdos_renyi_graph(10, 0.5)
randomGraph2 = nx.erdos_renyi_graph(5, 1.0, seed=1)
BA = nx.barabasi_albert_graph(100, 5, seed=1)
# print(CG)
# nx.draw_shell(BA, with_labels=True)
# nx.draw(BA, with_labels=True)
# plt.savefig("filename6.png")
#nx.write_edgelist(BA, "BA.edgelist")

newBA = nx.read_edgelist("BA.edgelist")
