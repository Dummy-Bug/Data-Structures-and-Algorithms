# https://practice.geeksforgeeks.org/problems/distance-from-the-source-bellman-ford-algorithm/0/#

class Solution:
    '''
    V: nodes in graph
    adj: adjacency list for the graph
    S: Source
    '''
    def bellman_ford(self, V, adj, S):
        
        infinity = 100000000
        dist = [infinity for i in range(V)]
        
        dist[S] = 0 # making distance of Source Zero
        
        for _ in range(V-1):
            
            for u,v,w in adj:
                
                if dist[u] + w < dist[v]: # then relax the edge
                    dist[v] = dist[u] + w
        # The distance Array would be nothing but the shortest distance
        # from S to all other Vertices
        return dist