# 1. Eigenvector Merkeziyet Ölçütü Hesaplama (2-3 kişi)
# a. Eigenvector merkeziyet ölçütünün başlangıç vektörünü sabit (hepsi 1), derece,
# yakınlık ve aradalık ölçütleri ile ayrı ayrı belirleyip yönlü ve yönsüz üçer graf üzerinde
# eigenvector merkeziyeti hesaplatmak.
# b. Eigenvector değerlerinin; derece, yakınlık ve aradalık değerleri ile korelasyonunu
# hesaplatmak
# 5 tane yönlü, 5 tane yönsüz graf için; birli, ikili, üçlü, dörtlü ve beşli ayıran düğüm
# kümelerindeki düğümlerin derece, aradalık, yakınlık, eigenvector ve pagerank
# değerlerini hesaplamak.


import networkx as nx
import csv
import numpy as np
import math
from networkx.utils import not_implemented_for


G1 = nx.barbell_graph(50, 2)
G2 = nx.lollipop_graph(100, 2)
G3 = nx.erdos_renyi_graph(100, 7)
G4 = nx.barabasi_albert_graph(100, 7)
G5 = nx.turan_graph(100, 7)

G1 = nx.to_directed(G1)
G2 = nx.to_directed(G2)
G3 = nx.to_directed(G3)
G4 = nx.to_directed(G4)
G5 = nx.to_directed(G5)


list0 = []
list1 = []
list2 = []
list3 = []
list4 = []


def find_node_cut(G):

    for i in range(5):
        x = i+1
        nodecut = list(nx.all_node_cuts(G, x))

        for k in range(len(nodecut)):

            for d in nodecut[k]:
                if i == 0:
                    list0.append(d)
                if i == 1:
                    list1.append(d)
                if i == 2:
                    list2.append(d)
                if i == 3:
                    list3.append(d)
                if i == 4:
                    list4.append(d)


def measurements(G, list):

    degerler = []
    for i in range(len(list)):

        derece = nx.degree_centrality(G)
        degerler.append(derece)
        print(list[i], "-> derece merkeziyeti=", derece[list[i]])

        yakinlik = nx.closeness_centrality(
            G, u=list[i], distance=None, wf_improved=True)
        degerler.append(derece)
        print(list[i], "-> yakınlık merkeziyeti=", yakinlik)

        eigen = nx.eigenvector_centrality(G)
        degerler.append(derece)
        print(list[i], "-> eigen değeri=", eigen[list[i]])

        betweenness = nx.betweenness_centrality(
            G, k=None, normalized=True, weight=None, endpoints=False, seed=None)
        degerler.append(derece)
        print(list[i], "-> aradalık merkeziyet=",
              betweenness[list[i]])

        pg = nx.pagerank(G1, alpha=0.85, personalization=None, max_iter=100,
                         tol=1e-06, nstart=None, weight='weight', dangling=None)
        degerler.append(derece)
        print(list[i], "-> pagerank=", pg[list[i]])

    print("-------------------------------------------------------------------", "\n")
    return degerler


"""
find_node_cut(G1)
print("Tekli ayıran düğümler= ", list0)
measurements(G1, list0)
print("İkili ayıran düğümler= ", list1)
measurements(G1, list1)
print("Üçlü ayıran düğümler= ", list2)
measurements(G1, list2)
print("Dörtlü ayıran düğümler= ", list3)
measurements(G1, list3)
print("Beşli ayıran düğümler= ", list4)
measurements(G1, list4)
list0.clear()
list1.clear()
list2.clear()
list3.clear()
list4.clear()


find_node_cut(G2)
print("Tekli ayıran düğümler= ", list0)
measurements(G2, list0)
print("İkili ayıran düğümler= ", list1)
measurements(G2, list1)
print("Üçlü ayıran düğümler= ", list2)
measurements(G2, list2)
print("Dörtlü ayıran düğümler= ", list3)
measurements(G2, list3)
print("Beşli ayıran düğümler= ", list4)
measurements(G2, list4)
list0.clear()
list1.clear()
list2.clear()
list3.clear()
list4.clear()

find_node_cut(G3)
print("Tekli ayıran düğümler= ", list0)
measurements(G3, list0)
print("İkili ayıran düğümler= ", list1)
measurements(G3, list1)
print("Üçlü ayıran düğümler= ", list2)
measurements(G3, list2)
print("Dörtlü ayıran düğümler= ", list3)
measurements(G3, list3)
print("Beşli ayıran düğümler= ", list4)
measurements(G3, list4)
list0.clear()
list1.clear()
list2.clear()
list3.clear()
list4.clear()

find_node_cut(G4)
print("Tekli ayıran düğümler= ", list0)
measurements(G4, list0)
print("İkili ayıran düğümler= ", list1)
measurements(G4, list1)
print("Üçlü ayıran düğümler= ", list2)
measurements(G4, list2)
print("Dörtlü ayıran düğümler= ", list3)
measurements(G4, list3)
print("Beşli ayıran düğümler= ", list4)
measurements(G4, list4)
list0.clear()
list1.clear()
list2.clear()
list3.clear()
list4.clear()

find_node_cut(G5)
print("Tekli ayıran düğümler= ", list0)
measurements(G5, list0)
print("İkili ayıran düğümler= ", list1)
measurements(G5, list1)
print("Üçlü ayıran düğümler= ", list2)
measurements(G5, list2)
print("Dörtlü ayıran düğümler= ", list3)
measurements(G5, list3)
print("Beşli ayıran düğümler= ", list4)
measurements(G5, list4)
list0.clear()
list1.clear()
list2.clear()
list3.clear()
list4.clear()
"""
find_node_cut(G1)
print("Tekli ayıran düğümler= ", list0)
measurements(G1, list0)
print("İkili ayıran düğümler= ", list1)
measurements(G1, list1)
print("Üçlü ayıran düğümler= ", list2)
measurements(G1, list2)
print("Dörtlü ayıran düğümler= ", list3)
measurements(G1, list3)
print("Beşli ayıran düğümler= ", list4)
measurements(G1, list4)
list0.clear()
list1.clear()
list2.clear()
list3.clear()
list4.clear()


find_node_cut(G2)
print("Tekli ayıran düğümler= ", list0)
measurements(G2, list0)
print("İkili ayıran düğümler= ", list1)
measurements(G2, list1)
print("Üçlü ayıran düğümler= ", list2)
measurements(G2, list2)
print("Dörtlü ayıran düğümler= ", list3)
measurements(G2, list3)
print("Beşli ayıran düğümler= ", list4)
measurements(G2, list4)
list0.clear()
list1.clear()
list2.clear()
list3.clear()
list4.clear()

find_node_cut(G3)
print("Tekli ayıran düğümler= ", list0)
measurements(G3, list0)
print("İkili ayıran düğümler= ", list1)
measurements(G3, list1)
print("Üçlü ayıran düğümler= ", list2)
measurements(G3, list2)
print("Dörtlü ayıran düğümler= ", list3)
measurements(G3, list3)
print("Beşli ayıran düğümler= ", list4)
measurements(G3, list4)
list0.clear()
list1.clear()
list2.clear()
list3.clear()
list4.clear()

find_node_cut(G4)
print("Tekli ayıran düğümler= ", list0)
measurements(G4, list0)
print("İkili ayıran düğümler= ", list1)
measurements(G4, list1)
print("Üçlü ayıran düğümler= ", list2)
measurements(G4, list2)
print("Dörtlü ayıran düğümler= ", list3)
measurements(G4, list3)
print("Beşli ayıran düğümler= ", list4)
measurements(G4, list4)
list0.clear()
list1.clear()
list2.clear()
list3.clear()
list4.clear()

find_node_cut(G5)
print("Tekli ayıran düğümler= ", list0)
measurements(G5, list0)
print("İkili ayıran düğümler= ", list1)
measurements(G5, list1)
print("Üçlü ayıran düğümler= ", list2)
measurements(G5, list2)
print("Dörtlü ayıran düğümler= ", list3)
measurements(G5, list3)
print("Beşli ayıran düğümler= ", list4)
measurements(G5, list4)
list0.clear()
list1.clear()
list2.clear()
list3.clear()
list4.clear()
