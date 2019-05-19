import numpy as np
import pandas as pd
import networkx as nx
import datetime
import datetime
import heapq
import scipy as sp
import heapq
import math

starttime = datetime.datetime.now()

G=nx.Graph()
path="C:/Users/Qiu/Desktop/proj3/data/training.txt"
cor ="C:/Users/Qiu/Desktop/proj3/data/core_nodes.txt"
vall= "C:/Users/Qiu/Desktop/proj3/data/val.txt"
task = open('C:/Users/Qiu/Desktop/' + 'niuniu' + '.txt','w')
dataset=np.loadtxt(path)
corenodes=np.loadtxt(cor)
vall =np.loadtxt(vall)
aa= np.array([10819.0,25875.0])
corenodes = np.setdiff1d(corenodes,aa)
# corenodes =corenodes.tolist()
print(len(corenodes))

a1 =dataset[:,0]
a2=dataset[:,1]
# val=vall[:,0]
val=vall[:,0]
val2=vall[:,1]

for i in val2:
    np.append(val,i)
val =set(val)

for i in range(len(dataset)):
   G.add_edge(int(a1[i]),int(a2[i]))

def nonedges(G,u):  #a generator with (u,v) for every non neighbor v
   for v in nx.non_neighbors(G, u):
       yield (u, v)

rr=[]
# for i in corenodes:
#     if i not in dataset:
#         print(i)
# for test
# for i in corenodes:
#    preds = nx.adamic_adar_index(G,nonedges(G,i))
#    tenlargest = heapq.nlargest(100, preds, key = lambda x: x[2])
#    for j in tenlargest:
#        rr.append(j)
# print(len(rr)) #==21550
# result= heapq.nlargest(4000, rr, key = lambda x: x[2])

#for val
for i in val:
   preds = nx.adamic_adar_index(G,nonedges(G,i))
   tenlargest = heapq.nlargest(1000, preds, key = lambda x: x[2])
   for j in tenlargest:
       rr.append(j)
print(len(rr)) #==21550
result= heapq.nlargest(2000, rr, key = lambda x: x[2])


endtime = datetime.datetime.now()
print ("time",(endtime - starttime).seconds)

count=0
for i in result:
   if i[2] ==0:
       count+=1
print(count)
print(len(result))
print(result,file=task)

###################################################################
