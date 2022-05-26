# https://leetcode.com/problems/is-graph-bipartite/
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        
        n = len(graph) # get all the vertices
        
        self.color = [-1]*n
        
        for i in range(n):
            
            if self.color[i] == -1:
                
                self.color[i] = 0
                if self.dfs(i,graph) == False:
                    return False
        
        return True
    
    
    def dfs(self,u,graph):
        
        for v in graph[u]:
            
            if self.color[v] == -1: # node is yet to visit
                
                self.color[v] = (self.color[u] + 1)%2 # we can also fo 1-self.color[u]
                if self.dfs(v,graph) == False:
                    return False
            
            else:
                if self.color[v] == self.color[u]:
                    return False
        
        return True