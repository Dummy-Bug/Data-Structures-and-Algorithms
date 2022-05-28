# https://practice.geeksforgeeks.org/problems/minimum-spanning-tree/1#

"""
T(c) = O(V^2)

"""
class Solution:
    
    def spanningTree(self, V, adj):
        
        # print(adj)
        cost = [float('inf') for i in range(V)]
        cost[0] = 0
        visited = set()
        parent  = [-1]*V
        
        # we need atleast n-1 edges to get minimum sum of edges.
        
        for i in range(V-1):
            
            mini = float("inf")
            
            for i in range(V):#find the minimum cost vertex
                if i not in visited and cost[i] < mini:
                    mini = cost[i]
                    u = i
                    
            visited.add(u) # Adding the vertex to set
            
            # now get all the adjacent vertices and try to relax them
            
            for neighbor in adj[u]:
                vertex,weight = neighbor
                
                if vertex not in visited and cost[vertex] > weight:
                    
                    cost[vertex]   = weight
                    parent[vertex] = u
        result = 0 
        for i in range(1,len(parent)):# we ommit first parent as it 
                                      # will alwyas be -1
            for neighbor in adj[parent[i]]:
                vertex,weight = neighbor
                if vertex == i:
                    result = result + weight 
        
        return result