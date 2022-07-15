import networkx as nx
"""
G = nx.path_graph(4)
G.add_edge(4, 5)
print(nx.is_connected(G))
print(nx.number_connected_components(G))
print(list(nx.connected_components(G)))
print(nx.node_connected_component(G, 5))
"""

DG = nx.DiGraph()
DG.add_edges_from([(1, 2), (1, 3)])

G3 = nx.complete_graph(5)
DG2 = nx.to_directed(G3)

print(nx.is_strongly_connected(DG))
print(nx.is_strongly_connected(DG2))

print(nx.is_weakly_connected(DG))
print(nx.is_weakly_connected(DG2))
