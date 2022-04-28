def addNodes(edges,w=[]):
    G={}
    for e in edges:
        if e[0] not in G:
            G[e[0]]=w
        if e[1] not in G:
            G[e[1]]=w
    return G
        
def addEdges(G,edges):
    for e in edges:
        try:
            G[e[0]]=G[e[0]]+[(e[1],e[2])]
            G[e[1]]=G[e[1]]+[(e[0],e[2])]
        except:
            print(e)
    return G

def tocap(g):
    G={}
    for i in g:
        for j in g[i]:
            k=[]
            if type(j)==str:
                k.append(j.capitalize())
        G[i.capitalize()]=k
    return G

Edgelist=[
#floor1
('gate 2', 'main Entrance', 0), ('gate 2', 'MPR main Entrance', 0), ('MPR Exit', 'turnstill', 0), ('main Entrance', 'Reception', 0), 
('vending Machine', 'Reception', 0), ('Student Center', 'Reception', 0), ('main Entrance', 'turnstill', 0), ('main Entrance', 'vending Machine', 0),
('Office Of Career Services', 'vending Machine', 0), ('Office Of Career Services', 'elevator 1', 0), ('Office Of Career Services','Reception',0),
('Office Of Career Services', 'Student Center', 0), ('elevator 1', 'vending Machine', 0), ('washroom1 (Reception)','Reception', 0), 
('washroom 1 (Reception)', 'Student Center', 0), ('washroom1 (Reception)', 'turnstill', 0), ('turnstill','Stairs 1 guest', 0), 
('turnstill','Stairs 2 to basement', 0), ('turnstill', 'cafe2go', 0), ('info commons', 'cafe2go', 0), ('turnstill','central street faculty pod',
0), ('turnstill', 'Student life', 0), ('health and wellness Center', 'Student life', 0),('faculty pod central street','Student life', 0),
('info commons','elevator 2', 0), ('elevator 2','writing Center', 0), ('info commons', 'Stairs 3', 0), ('library 1st floor', 'Stairs 3', 0),
 ('cafe2go', '---', 0), ('cafe2go','Ramp 1 to basement', 0),('faculty pod central street','Ramp 2 to courtyards', 0), ('central street faculty pod', 'Stairs 5 to 1st floor baithak',0),
('faculty pod central street', 'Stairs 3 to tapal', 0),('faculty pod central street', 'Stairs 4 to Courts', 0), ('faculty pod central street',
'Ramp 4 to Courts', 0),('Courts','Ramp 4 to Courts', 0),('faculty pod by Courts','Ramp 4 to Courts',0),('faculty pod by Courts',
'Stairs 4 to Courts',0),('Courts','Stairs 4 to Courts',0),('Student lounge','Ramp 4 to Courts',0),('Student lounge','Stairs 4 to Courts',0),
#floor 0
('music room','Stairs 2 to basement', 0),('music room','linux and networking lab', 0),('circuits and electronic lab 1','linux and networking lab',0),
('tapal','amphi theatre',0),('tapal','hu Dukaan',0),('Raheem Bhai','hu Dukaan',0),('Raheem Bhai','Garden area',0),('Raheem Bhai','dhaba',0),
('Raheem Bhai','Ramp 5 to Courts',0),('Courts','Garden area',0),('Stairs 6 to Courts thru Garden','Garden area',0),('zen Garden','Garden area',
0),('Courts','Ramp 5 to Courts',0),('Courts','zen Garden',0),('amphi theatre','gym',0),('foosball','gym',0),('foosball','table tennis',0),('table tennis','lost and found',
0),
#floor 2                                                            
('Stairs 5 (to baithak) up','tariq rafi',0),('film studio','tariq rafi',0),('mehfil','tariq rafi',0),('Stairs 5 (to baithak) up',
'faculty pod w221',0),('faculty pod w221','w242',0),('w242','w243',0),('w242','w244',0),('baithak','w242',0),('faculty pod w221','w234',0),
('faculty pod w221','elevator 2',0),('stairs 6 up','elevator 2',0),('stairs 6 up','central street 2',0),('faculty pod baithak c203',
'elevator 2',0),('faculty pod baithak c203', 'central street 2',0),('central street 2','mpr street 2',0),
('cpe classroom','mpr street 2',0),('n220','Deans Pod',0),('mpr street 2','elevator 1',0),('mpr street 2','n220',0),('n219','n220',0),
('deans pod','huf',0),
('n220','Faculty Pod n200',0),('mpr','bridge to lib 1st floor'),('mpr street 1','bridge to lib 1st floor'),('mpr street 1','elevator 1',0),
('mpr street 1','stairs 7 (to pg)',0),('bridge to lib 1st floor','library 1st floor',0),('dicussions area','library 1st floor',0),
('dicussions area','yohsin',0),('dicussions area','discussion rooms',0),('library 1st floor back','film studio',0),('central street 2','cpe',0),
('central street 2','cpe classroom',0),('audi','cpe classroom',0),('Stairs 6 to pg','cpe classroom',0),('elevator 1','cpe classroom',0),
('Stairs 6 to pg','pg',0),('pg','admin office',0)
#floor 3
]
g=addNodes(Edgelist,[])
addEdges(g,Edgelist)
G=tocap(g)
print(G)
