class Solution:
    
    def __init__(self):
        from collections import deque
        
    def isBipartite(self, graph: List[List[int]]) :
        
        n = len(graph)
        self.visited = [False for i in range(n)]
        self.color = [-1 for i in range(n)]
        
        for i in range(n):
            if self.visited[i] == False:
                if self.bfs(i,graph) == False:
                    return False
        return True
                
                
    def bfs(self,u,graph):
        
        self.color[u] = 0
        q = deque()
        q.append(u)
        c = 0
        
        while q:
            ln = len(q)
            
            for i in range(ln):
                u = q.popleft()
                self.visited[u] = True
                
                for v in graph[u]:
                    
                    if self.visited[v] == False:
                        
                        if self.color[v] == self.color[u]:
                            return False
                        
                        self.color[v] = (self.color[u] + 1)%2
                        q.append(v)
        return True
                        