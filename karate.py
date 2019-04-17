from sklearn import cluster
import networkx as nx
from collections import defaultdict
import matplotlib.pyplot as plt
from matplotlib import cm
import seaborn as sns
import pandas as pd
import numpy as np
from sklearn.metrics.cluster import normalized_mutual_info_score
from sklearn.metrics.cluster import adjusted_rand_score

G=nx.read_gml('./Data/karate/karate.gml',label='id')
# G = nx.karate_club_graph()


def graph_to_edge_matrix(G):
    edge_mat = np.zeros((len(G), len(G)), dtype=int)

    # Loop to set 0 or 1 (diagonal elements are set to 1)
    # for node in G:
    #     for neighbor in G.neighbors(node):
    #         edge_mat[node][neighbor] = 1
    #     edge_mat[node][node] = 1
    for node in G:
        for neighbor in G.neighbors(node):
            edge_mat[node-1][neighbor-1] = 1
        edge_mat[node-1][node-1] = 1

    return edge_mat

k_clusters = 2
results = []
algorithms = {}

edge_mat=graph_to_edge_matrix(G)

algorithms['kmeans'] = cluster.KMeans(n_clusters=k_clusters, n_init=200)
algorithms['agglom'] = cluster.AgglomerativeClustering(n_clusters=k_clusters, linkage="ward")
algorithms['spectral'] = cluster.SpectralClustering(n_clusters=k_clusters, affinity="precomputed", n_init=200)
# algorithms['affinity'] = cluster.AffinityPropagation(damping=0.6)
model=algorithms['kmeans'] .fit(edge_mat)
bb=list(model.labels_)
print(bb)

dic = {1: [], 0: []}
for i in range(34):
    if bb[i] == 1:
        dic[1].append(i)
    if bb[i] == 0:
        dic[0].append(i)

print(dic)
# em=graph_to_edge_matrix(G)
# Fit all models
# for model in algorithms.values():
#     model.fit(em)
#     results.append(list(model.labels_))
print(nx.degree(G))
print(nx.number_of_nodes(G))
print(nx.number_of_edges(G))

# a=[]
# # print(dic)
# for i in results:
#     dic = {1: [], 0: []}
#     for j in range(34):
#         if i[j]==1:
#             dic[1].append(j)
#         if i[j]==0:
#             dic[0].append(j)
#     a.append(dic)

# print(results)
