####################pagerank#############################################
import numpy as np
import pandas as pd
import networkx as nx
import datetime
import datetime
import heapq
import scipy as sp
import math
G1=nx.DiGraph()
for i in range(len(dataset)):
   G1.add_edge(int(id[i]),int(connection[i]))
   G1.add_edge(int(connection[i]),int(id[i]))

print(nx.number_of_nodes(G1))
mat= np.zeros([nx.number_of_nodes(G1), nx.number_of_nodes(G1)], dtype = float)

adj=G1.adj
nnode=nx.number_of_nodes(G1)
pr=dict.fromkeys(G1,float(1/nnode))
伪= 0.85
饾浗 = 0.15
max_iter=100
min_delta=0.00001
counter=0
for i in range(20):
    counter+=1
    change=0
    for k in adj:
        rank = 0
        for v in adj[k]:
            rank+=伪*pr[v]/len(adj[v])
        rank+=饾浗
        change+=abs(pr[k]-rank)
        pr[k]=rank
    if change<min_delta:
        break
# print(counter)
pagerank=sorted(pr.items(), key=lambda d: d[1],reverse=True)

topp=[]
for i in range(10):
   topp.append(pagerank[i][0])
b=nx.pagerank(G1)
zz=sorted(b.items(), key=lambda d: d[1],reverse=True)
pagerank=[]
for i in range(10):
    pagerank.append(zz[i][0])
print(pagerank,file=task)
