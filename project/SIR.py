# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 14:39:36 2020

@author: Mehmet ŞİMŞEK
"""
import networkx as nx
import ndlib.models.ModelConfig as mc
import ndlib.models.epidemics as ep
from collections import Counter
import numpy as np
from scipy.stats import linregress
import math

import pandas as pd

# Graf oluştur ve kenar listesi formatında bir dosyaya yaz
BG = nx.barbell_graph(30, 2)
nx.write_edgelist(BG, "BG")


# Aynı isimde bir csv dosyası oluşturup bütün sonuçları o dosyaya yazacağız.
dataset = "BG"
csv = dataset+".csv"
print(dataset)
# Veri setini oku. Yönlü ya da yönsüz olmasına göre aşağıdakilerden uygun olanı seç.
#G = nx.read_edgelist(dataset,nodetype=int, delimiter=" ",create_using=nx.DiGraph,data=False)
G = nx.read_edgelist(dataset, nodetype=int, delimiter=" ", data=False)

# Self loop içeren verisetleri için aşağıdaki kodun çalıştırılması gerekli.
# G.remove_edges_from(nx.selfloop_edges(G))


class Simulation:
    def RunSim(self, beta):
        SIR_ = {}  # düğüme karşılık düğümün etkisini tutan sözlük
        sayac = 0
        for node in G.nodes():
            # sayac=sayac+1
            # print(sayac) # Kaçıncı düğümde olduğunu görmek için kullanılabilir.
            model1 = ep.SIRModel(G)
            # Başlangıçta hangi düğümler Infected olacaksa bu liste ile belirleniyor. Yukarıdaki for dönüsü bütün düğümler için tek tek çalıştığından dolayı her seferinde 1 düğüm Infected olarak belirleniyor. Birden fazla düğüm de aynı anda Infected olarak belirlenebilir.
            seeds = [node]
            # print("Seed",seeds)
            # Model Configuration
            cfg = mc.Configuration()
            # Enfekte olma olasığını parametre olarak göndereceğiz
            cfg.add_model_parameter('beta', beta)
            # Bu değer genelde 1.0 alınır. Böylece, enfekte olan bir düğümün yalnızca bir iterasyon için komşu düğümleri enfekte etme olasılığı olur; çünkü diğer iterasyonda 1.0 olasılıkla (yani kesin) Recovered durumuna geçer.
            cfg.add_model_parameter('gamma', 1.0)
            cfg.add_model_initial_configuration("Infected", seeds)
            model1.set_initial_status(cfg)
            # Simulation execution
            seeds.clear()
            num_of_recovered_nodes = 0

            while True:  # Ağda enfekte düğüm kalmayana kadar simülasyonu çalıştırmak istiyoruz. İçeride bu durumu kontrol edip gerektiğinde döngüden çıkacağız.

                # Modeli bir iterasyon çalıştır.
                iterations = model1.iteration()
                #trends = model1.build_trends(iterations)
                ###############################################################
                # iterations sözlüğü S, I ve R durumlarında kaç düğüm var bunları tutar. ["node_count"] anahtarının 0. elemanı S durumunda olanların sayısını; 1. elemanı I durumunda olanların sayısını; 2. elemanı ise R durumunda olanların sayısını verir.
                ###############################################################

                # iterations["node_count"][1]==0 ise ağda enfekte düğüm kalmamıştır. Modellemeyi bitir.

                # Bir düğümün etkisi, bu düğüm tek başına Infected olarak seçildiğinde simülasyonun sonunda kaç düğümün R durumunda olduğudur. Aşağıdaki satırda bunu alıyoruz.
                if iterations["node_count"][1] == 0:
                    num_of_recovered_nodes = iterations["node_count"][2]
                    break

                # {Düğüm;Etki} sözlüğünü oluşturuyoruz.
            SIR_[node] = num_of_recovered_nodes  # total
            # print(num_of_recovered_nodes)
            iterations.clear()
        return SIR_


# ------------- Ağ için salgın eşik değerini hesapla
# Bir ağda salgın oluşması için Beta (enfekte etme olasaılığı) değerinin belirli bir eşik değerin üstüne olması gerekli.
# Aşağıdaki kısım bunu hesaplayıp beta_threshold değişkenine atıyor.
if nx.is_directed(G):
    total_degree = sum([pair[1] for pair in G.out_degree()])
    second_order_moment = sum([pair[1]*pair[1]
                              for pair in G.out_degree()])/len(G.nodes)
else:
    total_degree = sum([pair[1] for pair in G.degree()])
    second_order_moment = sum([pair[1]*pair[1]
                              for pair in G.degree()])/len(G.nodes)


degree_avg = total_degree/len(G.nodes())
beta_threshold = degree_avg/(second_order_moment-degree_avg)

betavalues = []
betavalues.append(math.ceil(10000*0.6*beta_threshold)/10000.0)
betavalues.append(math.ceil(10000*0.8*beta_threshold)/10000.0)
betavalues.append(math.ceil(10000*1.0*beta_threshold)/10000.0)
betavalues.append(math.ceil(10000*1.2*beta_threshold)/10000.0)
betavalues.append(math.ceil(10000*1.4*beta_threshold)/10000.0)
print("Average Degree: ", degree_avg)
print("Beta: ", betavalues)
# -------------------------------------------------------------

SIR = {}
for node in G.nodes():
    SIR[node] = 0

counter = 10  # Beklenen değer hesabı için simülasyon kaç kez tekrarlanacak? En az 10.000 olmalı


# Modellemeyi çalıştır
SM = Simulation()

# Sadece bir beta değeri için simülasyon yapıyoruz. Hesaplanan eşik değerin kendisini seçmek için 2. indekstekini aldık.
print("Beta: ", betavalues[2])
for turn in range(counter):
    print("Turn: ", turn)
    SIR_Temp = SM.RunSim(betavalues[2])
    for key in SIR_Temp.keys():
        SIR[key] = SIR[key]+SIR_Temp[key]/counter


# Merkeziyet Ölçütlerini hesapla
EC = nx.eigenvector_centrality(G)
print("Eigenvector finished")
DC = nx.degree_centrality(G)
print("Degree finished")
CC = nx.closeness_centrality(G)
print("Closeness finished")
BC = nx.betweenness_centrality(G)
print("Betweenness finished")

toplamdugumsayisi = len(G.nodes())
for i in SIR:
    SIR[i] = float(SIR[i]/toplamdugumsayisi)


# SIR sonuçlarını ve Merkeziyet Ölçütlerini bir PANDAS dataframe'de birleştir.

data_frame = pd.DataFrame(
    [[i] for i in range(G.number_of_nodes())], columns=['nodes'])


data_frame['SIR'] = data_frame['nodes'].map(SIR)


data_frame['EC'] = data_frame['nodes'].map(EC)
data_frame['DC'] = data_frame['nodes'].map(DC)
data_frame['CC'] = data_frame['nodes'].map(CC)
data_frame['BC'] = data_frame['nodes'].map(BC)

data_frame = data_frame.sort_values(by=['SIR'], ascending=False)
print(list(data_frame["nodes"][:10]))

data_frame.to_csv(csv, index=False, float_format='%.3f')
