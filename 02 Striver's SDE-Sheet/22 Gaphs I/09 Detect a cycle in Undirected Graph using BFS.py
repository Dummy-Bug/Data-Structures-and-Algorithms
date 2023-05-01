# https://practice.geeksforgeeks.org/problems/detect-cycle-in-an-undirected-graph/1#
class Solution:
    def isCycle(self, V, adj):
        
        self.parent  = [-1]*V
        self.color = ['white']*V
        
        for i in range(V):
            
            if self.color[i] == 'white':
                
                if self.bfs(i,adj):
                    return True

        return False
    
    def bfs(self,u,adj):
        
        from queue import Queue
        q = Queue(maxsize = 0)
        q.put(u)
        self.color[u] = 'grey'
        
        while q.empty() == False:
            u = q.get()
            for v in adj[u]:
                
                if self.color[v]!= 'white' and self.parent[u] != v:
                    return True
                    
                elif self.color[v] == 'white':
                    self.parent[v] = u
                    self.color[v] = 'grey'
                    q.put(v)
                        
        return False