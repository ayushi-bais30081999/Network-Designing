import networkx as nx
import matplotlib.pyplot as plot
import pandas as pd

parent = dict()
rank = dict()
sum=0

def make_set(v):    
    parent[v] = v
    rank[v] = 0    

def find(v):    
    if parent[v] != v:
        parent[v] = find(parent[v])
    return parent[v]

def union(v1, v2):    
    root1 = find(v1)
    root2 = find(v2)
    if root1 != root2:
        if rank[root1] > rank[root2]:
            parent[root2] = root1
        else:
            parent[root1] = root2
            if rank[root1] == rank[root2]: rank[root2] += 1

#algorithm for finding minimum cost of edges
def main(graph):
    for v in graph['v']:
        make_set(v)
    minimum_spanning_tree = set() 
    edges = sorted(graph['edges'], key=lambda e: e[2]) 
    for edge in edges:
        v1, v2, weight = edge
        if find(v1) != find(v2)
            union(v1, v2) 
            minimum_spanning_tree.add(edge)
    return sorted (minimum_spanning_tree) #return the set with minimum length

#pos of nodes (x-coordinate,y-coordinate) 
pos={0:(1800,10000),1:(500,9000),2:(5000,4500),3:(4000,8500),
     4:(100,5500),5:(0,2500),6:(1500,6500),7:(0,0),
     8:(1800,3500),9:(3000,3000),10:(2200,0),11:(3500,500)}

#label for every node in network
labels={0:'Pune',1:'Nagpur',2:'Mumbai',3:'Goa',4:'Ahemdabad',
        5:'Shimla',6:'Punjab',7:'Banglore',8:'Hyderabad',
        9:'Kerala',10:'Andra Pradesh',11:'Delhi'}

#intializing network
G=nx.Graph()
#draw node
nx.draw_networkx_nodes(G,pos,nodelist=[0,1,2,3,4,5,6,7,8,9,10,11],node_size=300,node_color='r')
#add labels to node
nx.draw_networkx_labels(G,pos,labels=labels,font_size=12,font_color='k',font_family='sans-serif',font_style='bold')
list_edges=[[0,1],[0,2],[0,3],[1,2],[1,4],[2,3],[2,1],[2,4],[2,6],[3,9],[4,2],[4,5],[5,6],[5,7],[6,7],[6,8],
            [7,8],[7,10],[8,9],[8,10],[9,11],[11,10]]
#adding edges
G.add_edges_from(list_edges)
print("Initial Network which connects all cities")
#draw network
nx.draw(G,pos,font_size=20,node_size=1500,node_color="#4CD1D8")
plot.show()

#giving input nodes & edges with cost
graph = {
    'v': [0,1, 2, 3, 4, 5, 6, 7, 8, 9,10,11],
    'edges': set([     
        (0,1,600),(0,2,600),(0,3,600),(1,2,100),(1,4,200),(2,3,200),(2,1,100),(2,4,700),
        (2,6,200),(3,9,1800),(4,2,700),(4,5,400),(5,6,1100),(5,7,1000),(6,7,2200),
        (6,8,500),(7,8,1200),(7,10,2500),(8,9,100),(8,10,600),(9,11,800),(11,10,500)])}
    
#calling main
a = main(graph)

#storing edges(with minimum length) in csvfile
with open('sample.csv','w') as f:
    for i in  a:
        p=str(i).strip('()')
        f.write(p)
        f.write('\n')
#retreiving edges(i.e. with minimum length) from csvfile        
df = pd.read_csv('sample.csv',usecols=[0,1])
e =df.values.tolist()
final = nx.Graph()
final.add_edge(0,1)
final.add_edges_from(e)
print("A Network which connects phone line with all cities and with minimum cost of phone line")
nx.draw_networkx_nodes(final,pos,nodelist=[0,1,2,3,4,5,6,7,8,9,10,11],node_size=300,node_color='b')
nx.draw_networkx_labels(final,pos,labels=labels,font_size=12,font_color='k')
#drawing final network
nx.draw(final,pos,node_size=1000,node_color='#4CD1D8',edge_color='#31087C',width=3.0)
plot.show()

#print the sum of minimum length of wire
for i in range(0,len(a)):
        sum=sum + a[i][2]
print("Minimum length of wire",sum) 

 
   







