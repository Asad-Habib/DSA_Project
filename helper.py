# Graph Helper Functions
def addNodes1(graph,x):
  G ={}
  for i in graph:
    G[i] = x
  return G

    
def get_neighbors(G, v):
    return G[v]

def dequeue(lst):
  x = lst.pop(0)
  return x

def out_edges(G,y):
    pp = []
    x = G[y]
    for p in x:
        pp.append(p)
    return pp

def enqueue(lst,x):
  counter = 0 
  lst.append(x)
  for i in range(len(lst)):
    if x[0] == lst[i][0]:
      if lst[i][1] > x[1]:
        lst[i] = x
        counter = 1
        break
    if counter == 0:
      lst.append(x)
  lst.sort(key=lambda x:x[1])
  return lst