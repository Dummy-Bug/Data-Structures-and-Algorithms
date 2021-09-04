class Solution:

	def isNegativeWeightCycle(self, n, edges):
		    
		dist = [float("inf") for i in range(n)]
		dist[0] = 0
		
		for _ in range(n-1):
		    
		    for u , v , w in edges:
		        if dist[u] + w < dist[v]:
		            dist[v] = dist[u] + w
		            
		for u,v,w in edges:

		    if  dist[u] + w < dist[v]:
		        return print("-ve cycle exist")
		
	    else:
		    return (print("No negative cycle exist"))