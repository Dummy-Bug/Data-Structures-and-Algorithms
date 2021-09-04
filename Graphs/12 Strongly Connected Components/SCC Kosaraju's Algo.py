class Solution:
    
    def __init__(self):
        
        from collections import defaultdict
        self.graph = defaultdict(list)
        
    def dfs(self,adj,u):
        
        self.visited[u] = True
        
        for padosi in adj[u]:
            
            if self.visited[padosi] == False:
                self.dfs(adj,padosi)
    
    def dfs_utility(self,adj,u):
        
        self.visited[u] = True
        
        for padosi in adj[u]:
        
            if self.visited[padosi] == False:
                self.dfs_utility(adj,padosi)
        
        self.stack.append(u)
            
    def transpose(self,adj,V):
        
        for i in range(V):
            for j in adj[i]:
                self.graph[j].append(i) # reversing the edge.
                
    def kosaraju(self, V, adj):
        
        self.visited =  [False for i in range(V)]
        self.stack = []
        
        for i in range(V):
            
            if self.visited[i] == False:
                self.dfs_utility(adj,i)
        
        self.transpose(adj,V)
        
        
        self.visited = [False for i in range(V)]
        result = 0
        
        while self.stack :
            
            u = self.stack.pop()
            
            if self.visited[u] == False:
                self.dfs(self.graph,u) # calling with Transposed graph
                
                result = result + 1
            
        return result