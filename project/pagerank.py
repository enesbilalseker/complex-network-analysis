import networkx as nx

G = nx.read_edgelist("Wiki-Vote.edgelist")
pr = nx.pagerank(G, alpha=0.85)
# print(pr)
print(nx.is_connected(G))
