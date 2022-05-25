# https://practice.geeksforgeeks.org/problems/bfs-traversal-of-graph/1
class Solution:
    def bfsOfGraph(self, V, adj):
        
        
        visited = dict()
        
        result = []
        self.bfs(V,adj,visited,result)
        return result
    
    def bfs(self,V,neighbors,visited,result):
        from collections import deque
        q = deque([0])
        visited[0] = True
        
        while q:
            vertex = q.popleft()
            
            for neighbor in neighbors[vertex]:
                
                if neighbor not in visited:
                    visited[neighbor] = True
                    q.append(neighbor)
                    
            result.append(vertex)
        return result