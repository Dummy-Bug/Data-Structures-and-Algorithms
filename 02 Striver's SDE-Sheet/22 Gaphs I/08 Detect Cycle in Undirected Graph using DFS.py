# https://practice.geeksforgeeks.org/problems/detect-cycle-in-an-undirected-graph/1#
class Solution:
    def isCycle(self, V, adj):
        
        self.color = ['white']*V
        
        for i in range(V): # This will make sure even if graph is
            if self.color[i] == 'white':# disconnected it finds the 
                if self.dfs(i,adj):# cycle
                    return True
        return False
                
    def dfs(self,u,adj,parent = None):
        self.color[u] = 'grey'
        
        for v in adj[u]:
            
            if self.color[v] == 'grey' and parent != v:
                
                return True
                
            elif self.color[v] == 'white':
                if self.dfs(v,adj,u):
                    return True
                
        return False