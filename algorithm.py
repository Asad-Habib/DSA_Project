from Edges import G,edges,addEdges,addNodes
from helper import get_neighbors
# This is heuristic function which has an equal values for all nodes, but because of its better choice of data structures, it is
# a lot more efficient than the djisktra algorithm (refer to comparealgorithm.py)
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
            if B==True: #if B is true then the output will contain bearings as well. If not, the default argument will just return the checkpoints.
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
