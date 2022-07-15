import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

G = nx.Graph()
G.add_nodes_from([0, 7])
G.add_edges_from([(0, 1), (1, 2), (1, 3), (1, 4), (1, 5),
                 (1, 6), (1, 7), (3, 7), (5, 2), (7, 5)])
print(G)
# nx.draw(G, with_labels=True)
# plt.savefig("filename7.png")
# degree = nx.degree_centrality(G)
# print(degree)

"""
DG = G.to_directed()
print(DG)
inDegree = nx.in_degree_centrality(DG)
outDegree = nx.out_degree_centrality(DG)
print(inDegree)
print(outDegree)
nx.draw(G, with_labels=True)
plt.savefig("filename8.png")
"""
completeGraph = nx.complete_graph(5)
er = nx.erdos_renyi_graph(5, 1)
er.add_node(6)  # graf bağlı değilse closeness hesaplanamaz.
path = nx.path_graph(11)

#closeness = nx.closeness_centrality(path)
# print(closeness)
#halter = nx.barbell_graph(5, 1)

#betweenness = nx.betweenness_centrality(path)
# print(betweenness)
ozvektor = nx.eigenvector_centrality(G)
print(ozvektor)
nx.draw(G, with_labels=True)
plt.savefig("filename11.png")
