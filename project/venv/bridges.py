import networkx as nx
import matplotlib.pyplot as plt
"""G = nx.lollipop_graph(11, 5)
G1 = nx.complete_graph(11)
G2 = nx.barbell_graph(5, 3)

kopruler = list(nx.bridges(G2))

print(kopruler)"""

G = nx.lollipop_graph(11, 5)
#node_cut = list(nx.minimum_node_cut(G))
kopruler = list(nx.bridges(G))


for i in kopruler:
    e = i
    G.remove_edge(*e)
