# https://practice.geeksforgeeks.org/problems/bfs-traversal-of-graph/1#

from queue import Queue
class Solution:
    def bfsOfGraph(self, V, adj):
        
        
        visited = [False for i in range(V)]
        result = []
        
        self.bfs(V,adj,visited,result)
        return result
    
    def bfs(self,V,neighbors,visited,result):
        
        q = Queue(maxsize=0) # initializing infinte sized queue
        q.put(0)
        visited[0] = True
        
        while (q.empty() == False):
            vertex = q.get()
            
            for neighbor in neighbors[vertex]:
                
                if visited[neighbor] == False:
                    visited[neighbor] = True
                    q.put(neighbor)
                    
            result.append(vertex)
        return 