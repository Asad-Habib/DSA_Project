"Graph Helper Functions"

def addNodes(G, nodes): # Takes a list of nodes, adds them to the graph. No edges
    for i in nodes:
        G[i] = []
    return G

def listOfNodes(G):
    return list(G.keys())


"""works without addNodes too"""
def addEdges(G, edges, directed = False): #Wtakes a list of edges, adds them to graph. 
    if directed:
        for i in edges:
            if i[0] in G:
                G[i[0]].append(i[1:])
            else:
                G[i[0]] = [i[1:]]
    else:
        for i in edges:

            if i[0] in G:
                G[i[0]].append(i[1:])
            else:
                G[i[0]] = [i[1:]]

            if i[1] in G:     
                G[i[1]].append((i[0],i[-1]))
            else:
                G[i[1]] = [(i[0],i[-1])]

    return G

def listOfEdges(G, directed): #has to be fixed, doesn't accept directed
    outedges= []
    for i in G:
        q = G[i]
        for x in G[i]:
            if (x[0], i, x[1]) not in outedges:
                outedges.append((i, x[0] ,x[1]))
    return outedges

def out_edges(Graph, i):
    accu = []
    for edge in Graph[i]:
        accu.append(edge[0])
    return accu

def printDegree(G):
    for i in G:
        x = G[i]
        print(i ,  "=>"     , len(x))

def printIn_OutDegree(G):
    out_degree,in_Degree=[],[]
    for a in G:
        out_degree.append(len(G[a]))
        for b in G[a]:

            in_Degree.append(b[0])
    count = 0
    for a in G:
        
        print(a," => In Degree: ",in_Degree.count(a),", Out Degree:",out_degree[count])
        count += 1

def getNeighbours(G,node):
    nodes = []
    keys = G[node]
    for a in keys:
        nodes.append(a[0])
    return nodes

def getInNeighbours(G,node):
    lst_neigh = []
    for i in G:
        for j in G[i]:
            if j[0]==node:
                lst_neigh.append(i)
    return lst_neigh

def NearestNeighbour(G,node):
    index = []
    weight = []
    for p in G[node]:
        index.append(p[0])
        weight.append(p[1])
    p = weight.index(min(weight))
    return index[p]

def isNeighbor(G, Node1, Node2):
    for x in G[Node1]:
        if x[0] == Node2:
            return True
        else:
            return False

def removeNode(G, node):
    G.pop(node)
    for i in G:
        for v in G[i]:
            if v[0] == node:
                G[i].remove(v)
    return G

def removeNodes(G, nodes):
    for node in nodes:
        G.pop(node)
        for i in G:
            for vv in G[i]:
                if vv[0] == node:
                    G[i].remove(vv)
    return G

def displayGraph(G):
    print(G)

def printadjmatrix(G):
    accu=[]
    x=listOfNodes(G)
    for alpha in range(len(x)):
      index=[]
      for b in range(len(x)):
        index.append(0)
      accu.append(index)
    for alpha in G:
      for b in G[alpha]:
        accu[alpha-1][b[0]-1]=b[1]
    return accu

def getOutNeighbours(G, node): # Returns all out neighbours in the node from graph
    index = []

    for x in G[node]:

        index.append(x[0])

    return index

#queue functions
def enqueue(q, item):
    q.append(item)
def dequeue(q):
    return q.pop(0)

