"""
171001020
Enes Bilal Şeker
Normal Öğretim
"""

import networkx as nx
import matplotlib.pyplot as plt

halter = nx.barbell_graph(11, 7)
nx.draw(halter, with_labels=True)
plt.savefig("gravitationalcentrality.png")
degree = nx.degree_centrality(halter)
values = {}

for source in halter:
    GC = 0
    for target in halter:
        if source != target:
            yol = nx.shortest_path_length(halter, source, target)
            GC = GC + ((degree[source] * degree[target]) / (yol * yol))
    values[source] = GC

print(values)
