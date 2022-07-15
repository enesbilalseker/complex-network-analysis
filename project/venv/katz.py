import networkx as nx
import math

G = nx.path_graph(4)
# phi = (1 + math.sqrt(5)) / 2.0  # largest eigenvalue of adj matrix
centrality = nx.katz_centrality(G)
# for n, c in sorted(centrality.items()):
#    print(f"{n} {c:.2f}")
print(centrality)
