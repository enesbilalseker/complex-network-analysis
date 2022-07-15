import networkx as nx

#G = nx.complete_graph(4)
#G1 = nx.path_graph(7)

# triangles = nx.triangles(G)
# print(triangles)
# print(kumelemeKatsayisi)

G = nx.lollipop_graph(11, 5)
tri = nx.triangles(G)
degree = nx.degree(G)
values = {}

for i in G:
    derece = degree[i]
    trii = tri[i]
    flag = derece - 1
    if(flag != 0):
        kumelemeKatsayisi = (trii*2)/((derece) * (derece - 1))
    values[i] = kumelemeKatsayisi

print(values)
print(nx.clustering(G))
