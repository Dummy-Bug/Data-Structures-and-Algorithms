# https://practice.geeksforgeeks.org/problems/minimum-spanning-tree/1#

"""
T(c) = O(NlogN). N iterations and logN for priority queue



"""
class Solution:
    
    def spanningTree(self, V, adj):

        cost = [float('inf') for i in range(V)]
        cost[0] = 0
        visited = set()
        result  = 0
        # we need atleast n-1 edges to get minimum sum of edges.
        import heapq
        heap = []
        heapq.heappush(heap,[cost[0],0])
        
        while heap: # Run V times if you want summ in this loop only
            
            weight,u = heapq.heappop(heap)
            
            if u in visited:
                continue
   
            visited.add(u) # Adding the vertex to set
            result = result + cost[u]
            # now get all the adjacent vertices and try to relax them
            
            for neighbor in adj[u]:
                vertex,weight = neighbor
                
                if vertex not in visited and cost[vertex] > weight:
                    
                    cost[vertex]   = weight
                    heapq.heappush(heap,[weight,vertex])
                    
        return result