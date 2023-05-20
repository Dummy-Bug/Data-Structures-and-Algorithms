class Solution:
    def isCyclic(self, V, adj):
        
        self.color = ['white']*V
        self.flag  = False
        
        for i in range(V):
            if self.color[i] == 'white':
                self.dfs(i,adj)
        
        
        return self.flag
        
    def dfs(self,u,adj):
           
        self.color[u] = 'grey'
        
        for v in adj[u]:
            if self.color[v] == 'grey':
                self.flag = True
            elif self.color[v] == "white":
                self.dfs(v,adj)
                
        self.color[u] = 'black'
