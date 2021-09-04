class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        self.seen = set()
        self.dx   = {}
        
        for edge in times:
            u,v,w = edge
            if u not in self.dx:
                self.dx[u] = []
            self.dx[u].append((v,w))
            
        # print(self.dx)
        
        self.cost = [float(inf) for i in range(n+1)]
        self.cost[0] = -1
        self.cost[k] = 0
        
        self.bfs(times,k)
        if len(self.seen)!=n:
            return -1
        return max(self.cost)
    
    def bfs(self,times,u):
        
        import heapq
        heap = []
        heapq.heappush(heap,[self.cost[u],u])
        
        while heap:
            prev_cost, u = heapq.heappop(heap)
            
            if u in self.seen:
                continue
            self.seen.add(u)
            
            if u not in self.dx:
                continue
                
            for padosi in self.dx[u]:
                v, w = padosi
                
                if v not in self.seen:
                    
                    self.cost[v] = min(self.cost[v], w + self.cost[u])
                    heapq.heappush(heap,[self.cost[v],v])