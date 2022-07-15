import networkx as nx
import matplotlib.pyplot as plt

G = nx.read_edgelist("facebook_combined.edgelist")

#nx.draw(G, with_labels=True)
# plt.savefig("facebook.png")

kopruler = list(nx.bridges(G))
print(kopruler)
print("---------------------------------------------------------------------------------------------------------------------------")
#node_cut = list(nx.minimum_node_cut(kopruler))
# print(node_cut)

for i in kopruler:
    pass
