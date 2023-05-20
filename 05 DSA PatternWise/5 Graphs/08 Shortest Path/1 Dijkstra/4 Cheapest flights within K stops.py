class Solution:
    
    def __init__(self):
        
        from collections import defaultdict
        
        self.graph = defaultdict(list)
        
    def bfs(self,src,dst,k):
        
        q = deque()
        q.append([0,src,-1])
        
        while q:
    
            dis , u , stops = q.popleft()
            
            if stops == k or u == dst:
                continue
                
            for v , w in self.graph[u]:        
                
                if self.distance[v] > dis + w :   # Don't use distance[u] + w 
                
                    self.distance[v] = dis+ w
                    q.append([self.distance[v],v,stops+1])
                        
        return self.distance[dst]      

                        

    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        for edge in flights: # O(E)
            u, v, w = edge
            
            self.graph[u].append([v,w])
            
        self.distance = [float("inf") for i in range(n)]
        self.visited  = [False for i in range(n)]
        
        self.distance[src] = 0
        
        result = self.bfs(src,dst,k)
        
        print(self.graph) 
        
        if  result == float("inf"):
            return -1
        
        else:
            return result
        
    