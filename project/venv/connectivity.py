# Flow-based Minimum Cuts
import networkx as nx
G = nx.complete_graph(7)
ayiranKenar = list(nx.minimum_edge_cut(G))
ayiranDugum = list(nx.minimum_node_cut(G))
print(ayiranKenar)
print(ayiranDugum)
