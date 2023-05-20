https://practice.geeksforgeeks.org/problems/minimum-spanning-tree/1?utm_source=gfg&utm_medium=article&utm_campaign=bottom_sticky_on_article

### Problem Description 

Given a weighted, undirected and connected graph of V vertices and E edges. The task is to find the sum of weights of the edges of the Minimum Spanning Tree.

 

Example 1:

Input:
3 3
0 1 5
1 2 3
0 2 1

Output:
4
Explanation:

The Spanning Tree resulting in a weight
of 4 is shown above.
Example 2:

Input:
2 1
0 1 5

Output:
5
Explanation:
Only one Spanning Tree is possible
which has a weight of 5.
 

Your task:
Since this is a functional problem you don't have to worry about input, you just have to complete the function  spanningTree() which takes number of vertices V and an adjacency matrix adj as input parameters and returns an integer denoting the sum of weights of the edges of the Minimum Spanning Tree. Here adj[i] contains a list of lists containing two integers where the first integer a[i][0] denotes that there is an edge between i and a[i][0][0] and second integer a[i][0][1] denotes that the distance between edge i and a[i][0][0] is a[i][0][1].

In other words , adj[i][j] is of form  { u , wt } . So,this denotes that i th node is connected to u th node with  edge weight equal to wt.

 

Expected Time Complexity: O(ElogV).
Expected Auxiliary Space: O(V2).
 

Constraints:
2 ≤ V ≤ 1000
V-1 ≤ E ≤ (V*(V-1))/2
1 ≤ w ≤ 1000
Graph is connected and doesn't contain self loops & multiple edges.


```

class Solution:
    
    def spanningTree(self, V, adj):

        cost = [float('inf') for i in range(V)]
        cost[0] = 0; visited = set()
        result  = 0
        # we need atleast n-1 edges to get minimum sum of edges.
        import heapq
        heap = []
        heapq.heappush(heap,[cost[0],0])
        
        while heap:
            
            weight,u = heapq.heappop(heap)
            
            if u in visited: # ignore the vertex if it is already added in MstSet
                continue
   
            visited.add(u) # Adding the vertex to Mstset
            result = result + cost[u]
            
            for neighbor in adj[u]:
                vertex,weight = neighbor
         
                if vertex not in visited and cost[vertex] > weight:
                    
                    cost[vertex]   = weight
                    heapq.heappush(heap,[weight,vertex])
                    
        return result

```
