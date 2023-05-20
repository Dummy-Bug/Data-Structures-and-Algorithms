https://practice.geeksforgeeks.org/problems/negative-weight-cycle3504/1

### Problem Description 

Given a weighted directed graph with n nodes and m edges. Nodes are labeled from 0 to n-1, the task is to check if it contains a negative weight 
cycle or not.
Note: edges[i] is defined as u, v and weight.
 

Example 1:

Input: n = 3, edges = {{0,1,-1},{1,2,-2},
{2,0,-3}}
Output: 1
Explanation: The graph contains negative weight
cycle as 0->1->2->0 with weight -1,-2,-3.
Example 2:

Input: n = 3, edges = {{0,1,-1},{1,2,-2},
{2,0,3}}
Output: 0
Explanation: The graph does not contain any
negative weight cycle.
 

Your Task:
You don't need to read or print anyhting. Your task is to complete the function isNegativeWeightCycle() which takes n and edges as input paramater and 
returns 1 if graph contains negative weight cycle otherwise returns 0.
 

Expected Time Complexity: O(n*m)
Expected Space Compelxity: O(n)
 

Constraints:
1 <= n <= 100
1 <= m <= n*(n-1), where m is the total number of Edges in the directed graph.

```


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
		    
		    
		    
```
