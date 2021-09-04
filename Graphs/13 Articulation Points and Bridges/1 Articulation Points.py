def ArticulationPoints(self,V,graph):
    
    self.visited = [False for i in range(V)]
    self.parent  = [-1 for i in range(V)]
    self.disc    = [float("inf") for i in range(V)] # dicovery time 
    self.low     = [floar("inf") for i in range(V)] 
    self.AP           = [False for i in range(V)] 
    self.time    = 0
    
    for i in range(V):
        if self.visited[i] == False:
            self.dfs(i,graph) # here graph is adjacency list
            
def dfs(self,u,graph):
    
    self.disc[u] = self.time 
    self.low[u]  = self.time
    self.time    = self.time + 1
    self.visited[u] = True
    children = 0 # to keep the count of number of children
    
    for v in graph[u]:
        
        if self.visited[v] == False:
            
            self.parent[v] = self.parent[u]
            children = children + 1
            self.dfs(v,graph)
            
            self.low[u] = min(self.low[u],self.low[v])
            
            # if u is an articulation point then it follows the following cases
            
            # (1) if node is a root node
            if self.parent[u] == -1 and children > 1:
                self.AP[u] = True
            # (2) if node is not root node and it's child has reach above it.
            if self.parent[u] != -1 and self.low[v] >= self.disc[u]:
                self.AP[u] = True
                
        elif v != self.parent[u]: # back edge
            self.low[u] = min(self.low[u] , self.disc[v])
    