# https://practice.geeksforgeeks.org/problems/topological-sort/1
class Solution:
    def topoSort(self, V, adj):
        
        self.time = 0
        self.start_time = [0 for i in range(V)]
        self.end_time   = [0 for i in range(V)]
        self.color       = ['white' for i in range(V)]
        
        for i in range(V):
            if self.color[i] == 'white':
                self.dfs(i,adj)
                
        result = []
        from collections import defaultdict
        dx = defaultdict()
        
        for i in range(len(self.end_time)):
            dx[self.end_time[i]] = i
        
        for i in sorted(self.end_time,):
            result.append(dx[i])
        return result[::-1]
            
        
    def dfs(self,u,adj):
        
        self.time += 1
        self.start_time[u] = self.time 
        self.color[u] = 'grey'
        
        for padosi in adj[u]:
            if self.color[padosi] == 'white':
                self.dfs(padosi,adj)
                
        self.time += 1
        self.end_time[u] = self.time
        self.color[u] = 'black'