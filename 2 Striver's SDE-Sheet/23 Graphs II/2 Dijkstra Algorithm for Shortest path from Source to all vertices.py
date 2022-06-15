# https://practice.geeksforgeeks.org/problems/implementing-dijkstra-set-1-adjacency-matrix/1

class Solution:
    def dijkstra(self, V, adj, s):
        
        visited = set()
        cost    = [float('inf') for i in range(V)]
        cost[s] = 0
        
        import heapq
        heap = []
        heapq.heappush(heap,[cost[s],s])
        
        while heap:
            prev_cost , u = heapq.heappop(heap)
            
            if u in visited:
                continue
            visited.add(u)
            
            for v , wt in adj[u]:
                if  v not in visited:
                    cost[v]    = min( wt + cost[u],cost[v] )
                    heapq.heappush(heap,[cost[v],v])
                    
        return cost 