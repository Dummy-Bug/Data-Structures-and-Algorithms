class Solution:
    def dfsOfGraph(self, V, adj):
        self.color = ['white']*V
        self.DFS   = []
        return self.dfs(0,adj)
    
    def dfs(self,u,adj):
        self.color[u] = 'grey'
        self.DFS.append(u)
        
        for v in adj[u]:
            if self.color[v] == 'white':
                self.dfs(v,adj)
        return self.DFS
