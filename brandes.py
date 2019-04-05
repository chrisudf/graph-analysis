import numpy as np
import pandas as pd
import networkx as nx
import datetime
import datetime
import heapq
import scipy as sp
import math

starttime = datetime.datetime.now()

G=nx.Graph()
path="C:/Users/Qiu/Desktop/project1/INFS7450-Project_One/data.txt"
task = open('C:/Users/Qiu/Desktop/' + 'result' + '.txt','w')
dataset=np.loadtxt(path)
id =dataset[:,0]
connection=dataset[:,1]
for i in range(len(dataset)):
    G.add_edge(int(id[i]),int(connection[i]))

Nbet=dict.fromkeys(G,0)
class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def empty(self):
        return self.size() == 0

    def size(self):
        return len(self.items)
#predecessor container
for i in G.nodes():
  pre= {w:[] for  w in G.nodes()}
  flag=dict.fromkeys(G,None)  #mark every node unvisited
  sp=dict.fromkeys(G,0)  #shortest path dict
  q=Queue()
  q.enqueue(i)
  flag[i]=0
  sp[i]=1
  bfs=[]
  while not q.empty():   #bfs search
      node=q.dequeue()
      bfs.append(node)
      for n in G.neighbors(node):
          if flag[n]==None:
              flag[n]=flag[node]+1
              q.enqueue(n)
          if flag[n]==flag[node]+1:
              sp[n]+=sp[node]
              pre[n].append(node)
  #backward step
  delta = dict.fromkeys(G, 0)    #initialize all delta value to 0,reserve the bfs based on predecessor
  for w in bfs[::-1]:
      for v in pre[w]:
          delta[v]+= sp[v]/sp[w]*(1+delta[w])
      if w!=i:                   #skip value of the begining node for forward step
          Nbet[w]+=delta[w]

a=sorted(Nbet.items(), key=lambda d: d[1],reverse=True)

top10=[]
for i in range(10):
   top10.append(a[i][0])

print(top10,file=task)

endtime = datetime.datetime.now()
print ("time",(endtime - starttime).seconds)

