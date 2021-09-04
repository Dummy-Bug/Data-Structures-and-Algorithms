from collections import deque

class Solution:
    def topoSort(self, V, adj):
        
        self.indegree = [0]*V
        
        for i in range(V):
            for padosi in adj[i]:
                self.indegree[padosi] += 1
                
        self.queue = deque() 
        for i  in range(V):
            
            if self.indegree[i] == 0:
                self.queue.append(i) 
                
        self.visited = [False for i in range(V)]
        
        return self.bfs(adj,[])
        
    def bfs(self,adj,result):
        
        while self.queue:
            
            u = self.queue.popleft()
            self.visited[u] = True
            result.append(u)
            for padosi in adj[u]:
                
                if self.visited[padosi] == False:
                    self.indegree[padosi] -= 1
                    
                    if self.indegree[padosi] == 0:
                        self.queue.append(padosi)
        return result
