class Solution:
    def dijkstra(self, V, adj, s):
        
        self.visited = [False for i in range(V)]
        self.cost    = [float('inf') for i in range(V)]
        self.cost[s] = 0
        
        import heapq
        heap = []
        heapq.heappush(heap,[self.cost[s],s])
        
        while heap:
            prev_cost , u = heapq.heappop(heap)
            
            if self.visited[u] == True:
                continue
            
            self.visited[u] = True
            
            for v , wt in adj[u]:
                if  self.visited[v] == False:
                    self.cost[v]    = min( wt + self.cost[u],self.cost[v] )
                    heapq.heappush(heap,[self.cost[v],v])
                    
        return self.cost