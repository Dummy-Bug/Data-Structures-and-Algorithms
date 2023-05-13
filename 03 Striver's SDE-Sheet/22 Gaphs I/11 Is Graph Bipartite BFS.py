# https://leetcode.com/problems/is-graph-bipartite/
class Solution:
        
    def isBipartite(self, graph: List[List[int]]) :
        
        n = len(graph)
        self.color   = [-1 for i in range(n)]
        
        for i in range(n):
            if self.color[i] == -1:
                if self.bfs(i,graph) == False:
                    return False
        return True
                
                
    def bfs(self,u,graph):
        
        from queue import Queue
        
        self.color[u] = 0
        q = Queue(maxsize = 0)
        q.put(u)
        
        while (q.empty() == False):
            
            u = q.get()
                
            for v in graph[u]:
                    
                if self.color[v] == -1:
                        
                    self.color[v] = (self.color[u] + 1)%2
                    q.put(v)
                    
                else:
                    if self.color[v] == self.color[u]:
                        return False
        return True