
class Solution:
    
    def bfsOfGraph(self, V, adj):
        self.color = ['white']*V
        return self.bfs(0)
        
    def bfs(self,u):
        from collections import deque
        BFS = []
        q = deque([])
        q.append(u)
        self.color[u] = 'grey'
    
        while q:
            u = q.popleft()
            
            for v in adj[u]:
                if self.color[v] == 'white':
                    q.append(v)
                    self.color[v] = 'grey'
        
            BFS.append(u)
        return BFS
