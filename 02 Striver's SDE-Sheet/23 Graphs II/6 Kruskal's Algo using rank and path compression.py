# https://practice.geeksforgeeks.org/problems/minimum-spanning-tree/1#
class Solution:
    def spanningTree(self, V, adj):
        
        # Using Kruskal's algo
        
        self.graph = []
        # make a graph containing [source,destination,weight]
        for u in range(V):
            for edge in adj[u]:
                self.graph.append([u,edge[0],edge[1]])
        
        # sort the edges according to the weight
        self.graph = sorted(self.graph,key = lambda x:x[2])
        
                    
        parent = [i for i in range(V)]
        rank   = [1 for i in range(V)] # every set will have atleast one node in it.
        i, e = 0, 0
        result = 0
        
        while e < V-1:
            u, v, w = self.graph[i]
            i = i + 1
            
            x = self.find_parent(parent,u)
            y = self.find_parent(parent,v)
            
            # if including this edge is not creating cycle then add it to the tree.
            
            if x != y:
                result = result + w
                e = e + 1
                self.union(x,y,parent,rank)
        return result 
    
    
    def find_parent(self,parent,i):
        if parent[i] == i:
            return i
        parent[i] = self.find_parent(parent,parent[i])
        return parent[i]
    
    def union(self,s1,s2,parent,rank):
        
        if rank[s1] < rank[s2]:
            parent[s1] = s2
            
        elif rank[s2] < rank[s1]:
            parent[s2] = s1
        
        else:
            parent[s2] = s1
            rank[s1]  += 1