def kruskal_algo(self,V): # V is the number of vertices
    # graph is list of lists containing all the edges: [source,destination,weight] 
    self.graph = sorted(self.graph,key= lambda x:x[2])
    
    parent = [i for i in range(V)]
    rank   = [1 for i in range(V)] # every set will have atleast one node in it.
    i, e = 0, 0
    result = []
    while e < V-1:
        u, v, w = self.graph[i]
        i = i + 1
        
        x = self.find_parent(parent,u)
        y = self.find_parent(parent,v)
        
        # if including this edge is not creating cycle then add it to the tree.
        
        if x != y:
            result.append([u,v,w])
            e = e + 1
            self.union(x,y,parent,rank)
    return result 


def find_parent(self,parent,i):
    if parent[i] == i:
        return i
    parent[i] = self.find_parent(parent,parent[i])
    return parent[i]

def union(u,v,parent,rank):
    
    s1 = find_parent(parent,u)
    s2 = find_parent(parent,v)
    
    if rank[s1] < rank[s2]:
        parent[s1] = s2
        rank[s1]   = rank[s1] + rank[s2]
    else:
        parent[s2] = s1
        rank[s1]   = rank[s1] + rank[s2]
