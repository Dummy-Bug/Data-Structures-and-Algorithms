class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int):
        
        self.seen = set()
        self.prob = [0 for i in range(n)]
        self.prob[start] = 1
        self.adj  = {}
        
        for i in range(len(edges)):
            edge = edges[i]
            u , v = edge
            
            if u not in self.adj:
                self.adj[u] = []
            self.adj[u].append([v,succProb[i]])
            
            if v not in self.adj:
                self.adj[v] = []
            self.adj[v].append([u,succProb[i]])

        self.bfs(start,end,succProb)
        
        return abs(self.prob[end])
    
    def bfs(self,start,end,succProb):
        
        import heapq
        heap = []
        heapq.heappush(heap,[-1,start])
        
        while heap:
            prob , u = heapq.heappop(heap)
            
            if u in self.seen:
                continue
            self.seen.add(u)
            
            if u not in self.adj:
                continue
                
            for padosi in self.adj[u]:
                v, prb = padosi
                
                if v not in self.seen:
                    self.prob[v] = max( abs(self.prob[v]) , abs(self.prob[u])*abs(prb) )
                    heapq.heappush(heap,[-self.prob[v],v])
        
            
            
            
            
            
            
            
            
            
            