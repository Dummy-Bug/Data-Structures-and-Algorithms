class Solution:
    def graph(self,edge):
        u, v = edge[0], edge[1]
        
        self.list[u].append(v)
        self.list[v].append(u)
    
    def dfs(self,u):
        self.visited[u] = True
        
        for padosi in self.list[u]:
            
            if self.visited[padosi] == False:
                self.dfs(padosi)
        
    
    def makeConnected(self, n, connections):

       # take any graph of n vertices we need atleast n-1 edges to make it connected.
        if n > len(connections)+1:
            return -1
      # observe carefully problem is nothing but finding the number of connected components.       
        
        self.visited = [False for i in range(n)]

     # just make the graph and traverse it using DFS/BFS 
        self.list = {} 
        for i in range(n):
            self.list[i] = []
            
        for edge in connections:
            self.graph(edge)
        result = -1
        for vertex in range(n):
            if self.visited[vertex] == False:
                self.dfs(vertex)
                result = result + 1
        return result
        