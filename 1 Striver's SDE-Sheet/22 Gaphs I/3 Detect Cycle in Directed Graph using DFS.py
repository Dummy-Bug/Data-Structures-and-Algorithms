# https://practice.geeksforgeeks.org/problems/detect-cycle-in-a-directed-graph/1
class Solution:
    
    def isCyclic(self, V, adj):

        self.color = ['white']*V

        for i in range(V):
            if self.color[i] == 'white':
                if self.dfs(i,adj):
                    return True
        return False

        
    def dfs(self,u,adj):
           
        self.color[u] = 'grey'
        
        for v in adj[u]:
            if self.color[v] == 'grey':
                return True
            elif self.color[v] == "white":
                if self.dfs(v,adj):
                    return True
                
        self.color[u] = 'black'