from Edges import G1,positions1,edges1, addNodes
from helper import enqueue,dequeue,get_neighbors,addNodes1
import math
import time
def dijkstra(graph,s,e):
  PQ=[]
  enqueue(PQ,(s,0))
  Dist=addNodes1(graph,math.inf)
  Dist[s]=0
  Prev=addNodes1(graph, None)
  while len(PQ)>0:
    u=dequeue(PQ)
    if u[0]==e:
      break
    children=get_neighbors(graph,u[0])
    for a in children:
      child,weight=a[0],a[1]
      alt=Dist[u[0]]+weight
      if alt<Dist[child]:
        Dist[child]=alt
        Prev[child]=u[0]
        enqueue(PQ,(child,alt))
  path=[]
  x=e
  while x!=None:
      path.append(x)
      x=Prev[x] 
  path.reverse()
  new = []
  for i in range(len(path)):
    if path[i]!= e:
      new+=[(path[i],path[i+1])]
  return new
djisktratime=time.time()
output=(dijkstra(G1,'Gate 2', 'ATM'))
djisktratime=time.time()-djisktratime
print("Djisktra execution time:",djisktratime)

stroutput=''
c=1
for a in range(len(output)):
    if a==0:
        stroutput+='Current Location: '+output[a][0]+'\n'
        stroutput+='Checkpoint '+str(c)+': '+output[a][1]+'\n'
        c+=1
    elif a==len(output)-1:
        stroutput+='Destination: '+output[a][1]+'\n'
    else:
        stroutput+='Checkpoint '+str(c)+': '+output[a][1]+'\n'
        c+=1
print(stroutput)

def h1(n,stop,positions):
    for i in positions:
        if i[0]==n:
            x1=i[1][0]
            y1=i[1][1]
        if i[0]==stop:
            x2=i[1][0]
            y2=i[1][1]
    return int(math.sqrt(abs(x2 - x1)*2 + abs(y2 - y1)*2))
def astar_algorithm(G, start, stop, positions):
#open_lst: a list of nodes which have been visited, but who's neighbours haven't all been always inspected, It starts off with the start node
#closed_lst: a list of nodes which have been visited and who's neighbors have been always inspected
    open_lst = set([start])
    closed_lst = set([])
    # the default value is +infinity
    dist={}#dist has present distances from start to all other nodes
    dist[start]=0
    path={}# path contains an adjac mapping of all nodes
    path[start]=start
    while len(open_lst) > 0:
        n=None
        for lowfv in open_lst:# it will find a node with the lowest value of f()
            if n==None or dist[lowfv]+h1(lowfv,stop,positions)<dist[n]+h1(n,stop,positions):
                n=lowfv
        if n==None:
            print('Path does not exist!')
            return None
        # if the current node is the stop then we start again from start
        if n==stop:
            reconst_path=[]
            while path[n]!=n:
                reconst_path.append(n)
                n=path[n]
            reconst_path.append(start)
            reconst_path.reverse()
            return reconst_path
        # for all the neighbors of the current node do
        for a in get_neighbors(G, n):
            m,weight=a[0],a[1]
# if the current node is not presentin both open_lst and closed_lst add it to open_lst and note n as it's path
            if m not in open_lst and m not in closed_lst:
                open_lst.add(m)
                path[m]=n
                dist[m] = dist[n] + weight
# otherwise, check if it's quicker to first visit n, then m and if it is, update path data and poo data
# and if the node was in the closed_lst, move it to open_lst
            else:
                if dist[m]>dist[n]+weight:
                    dist[m] = dist[n] + weight
                    path[m] = n
                    if m in closed_lst:
                        closed_lst.remove(m)
                        open_lst.add(m)
#remove n from the open_lst, and add it to closed_lst because all of his neighbors were inspected
        open_lst.remove(n)
        closed_lst.add(n)
    print('Path does not exist!')
    return None
astar_time=time.time()
output=(astar_algorithm(G1,'Gate 2', 'ATM',positions1))
astar_time=time.time()-astar_time
print("A* execution time:",astar_time)
stroutput=''
c=1
# for a in range(len(output)):
#     if a==0:
#         stroutput+='Here is your path followed by direction bearings!\nCurrent Location: '+output[a][0]+' '+output[a][1]+'\n'
#     elif a==len(output)-1:
#         stroutput+='Destination: '+output[a][0]+' '+output[a][1]+'\n'
#     else:
#         stroutput+='Checkpoint '+str(c)+': '+output[a][0]+' '+output[a][1]+'\n'
#         c+=1
# print(stroutput)
for a in range(len(output)):
    if a==0:
        stroutput+='Current Location: '+output[a]+'\n'
    elif a==len(output)-1:
        stroutput+='Destination: '+output[a]+'\n'
    else:
        stroutput+='Checkpoint '+str(c)+': '+output[a]+'\n'
        c+=1
print(stroutput)

def get_neighbors(G, v):
    return G[v]
# This is heuristic function which has an equal values for all nodes
def h(n,edges,start=0,end=0):
    H=addNodes(edges,1)
    return H[n]
def a_star_algorithm(G, start, stop, edges,B=False):
#open_lst: a list of nodes which have been visited, but who's neighbours haven't all been always inspected, It starts off with the start node
#closed_lst: a list of nodes which have been visited and who's neighbors have been always inspected
    open_lst = set([start])
    closed_lst = set([])
    # the default value is +infinity
    dist={}#dist has present distances from start to all other nodes
    dist[start]=0
    path={}# path contains an adjac mapping of all nodes
    path[start]=start
    while len(open_lst) > 0:
        n=None
        for lowfv in open_lst:# it will find a node with the lowest value of f()
            if n==None or dist[lowfv]+h(lowfv,edges)<dist[n]+h(n,edges):
                n=lowfv
        if n==None:
            print('Path does not exist!')
            return None
        # if the current node is the stop then we start again from start
        if n==stop:
            reconst_path=[]
            while path[n]!=n:
                reconst_path.append(n)
                n=path[n]
            reconst_path.append(start)
            reconst_path.reverse()
            if B==True:
                for a in range(len(reconst_path)):
                    for b in range(len(edges)):
                        if reconst_path[a]==edges[b][0]:
                            reconst_path[a]=(reconst_path[a],str(edges[b][3]))
            return reconst_path
        # for all the neighbors of the current node do
        for a in get_neighbors(G, n):
            m,weight=a[0],a[1]
# if the current node is not presentin both open_lst and closed_lst add it to open_lst and note n as it's path
            if m not in open_lst and m not in closed_lst:
                open_lst.add(m)
                path[m]=n
                dist[m] = dist[n] + weight
# otherwise, check if it's quicker to first visit n, then m and if it is, update path data and poo data
# and if the node was in the closed_lst, move it to open_lst
            else:
                if dist[m]>dist[n]+weight:
                    dist[m] = dist[n] + weight
                    path[m] = n
                    if m in closed_lst:
                        closed_lst.remove(m)
                        open_lst.add(m)
#remove n from the open_lst, and add it to closed_lst because all of his neighbors were inspected
        open_lst.remove(n)
        closed_lst.add(n)
    print('Path does not exist!')
    return None
a_star_time=time.time()
output=a_star_algorithm(G1,'Gate 2', 'ATM',edges1)
a_star_time=time.time()-a_star_time
print("A* with h=1 execution time:",a_star_time)
stroutput=''
c=1
for a in range(len(output)):
    if a==0:
        stroutput+='Current Location: '+output[a]+'\n'
    elif a==len(output)-1:
        stroutput+='Destination: '+output[a]+'\n'
    else:
        stroutput+='Checkpoint '+str(c)+': '+output[a]+'\n'
        c+=1
print(stroutput)
# output=a_star_algorithm(G,'Gate 2', 'Tapal 1',edges)
# stroutput=''
# c=1
# for a in range(len(output)):
#     if a==0:
#         stroutput+='Here is your path followed by direction bearings!\nCurrent Location: '+output[a][0]+' '+output[a][1]+'\n'
#     elif a==len(output)-1:
#         stroutput+='Destination: '+output[a][0]+' '+output[a][1]+'\n'
#     else:
#         stroutput+='Checkpoint '+str(c)+': '+output[a][0]+' '+output[a][1]+'\n'
#         c+=1
# print(stroutput)