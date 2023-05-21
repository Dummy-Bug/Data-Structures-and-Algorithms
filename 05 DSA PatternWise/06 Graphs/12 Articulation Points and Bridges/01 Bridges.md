```


def Bridges(self,V,graph):
    
    self.visited = [False for i in range(V)]
    self.parent  = [-1 for i in range(V)]
    self.disc    = [float("inf") for i in range(V)] # dicovery time 
    self.lowestReachableTime     = [float("inf") for i in range(V)] 
    self.brides  = []
    self.time    = 0
    
    for i in range(V):
        if self.visited[i] == False:
            self.dfs(i,graph) # here graph is adjacency list
            
def dfs(self,u,graph):
    
    self.disc[u] = self.time 
    self.lowestReachableTime[u]  = self.time
    self.time    = self.time + 1
    self.visited[u] = True
    
    
    for v in graph[u]:
        
        if self.visited[v] == False:
            
            self.parent[v] = self.parent[u]
            self.dfs(v,graph)
            
            self.lowestReachableTime[u] = min(self.lowestReachableTime[u],self.lowestReachableTime[v])

            if self.lowestReachableTime[v] >= self.disc[u]:
                self.bridges.append([u,v])
                
        elif v != self.parent[u]: # back edge
            self.lowestReachableTime[u] = min(self.lowestReachableTime[u] , self.disc[v])
    
    
    ```
