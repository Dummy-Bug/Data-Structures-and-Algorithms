class Solution:
    
    def isBipartite(self, graph: List[List[int]]) :
        
        n = len(graph)

        self.color = [-1 for i in range(n)]
        self.prev  = 0
        
        for i in range(n):
            
            if self.color[i] == -1:
                
                if self.dfs(i,graph) == False:
                    return False
                
        return True
                
                
    def dfs(self,u,graph):
        
        self.color[u] = (self.prev + 1 )%2
        
        for v in graph[u]:
            
            if self.color[v] == -1:
                
                self.prev = self.color[u]
                
                if self.dfs(v,graph) == False:
                    return False
                
            elif self.color[v] == self.color[u]:
                return False
        
        return True
                        