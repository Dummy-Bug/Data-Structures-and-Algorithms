https://practice.geeksforgeeks.org/problems/strongly-connected-components-kosarajus-algo/1?utm_source=gfg&utm_medium=article&utm_campaign=bottom_sticky_on_article

### Problem Description

Given a Directed Graph with V vertices (Numbered from 0 to V-1) and E edges, Find the number of strongly connected components in the graph.
 

Example 1:

Input:

Output:
3
Explanation:

We can clearly see that there are 3 Strongly
Connected Components in the Graph
Example 2:

Input:

Output:
1
Explanation:
All of the nodes are connected to each other.
So, there's only one SCC.
 

Your Task:
You don't need to read input or print anything. Your task is to complete the function kosaraju() which takes the number of vertices V and adjacency 
list of the graph as inputs and returns an integer denoting the number of strongly connected components in the given graph.
 

Expected Time Complexity: O(V+E).
Expected Auxiliary Space: O(V+E).
 

Constraints:
1 ≤ V ≤ 5000
0 ≤ E ≤ (V*(V-1))
0 ≤ u, v ≤ N-1
Sum of E over all testcases will not exceed 25*106



```


from collections import defaultdict;

class Solution:
    
    def __init__(self):
        self.reverseGraph = defaultdict(list);

    def dfs(self,graph,u):
        
        self.visited[u] = True;
        
        for padosi in graph[u]:
        
            if self.visited[padosi] == False:
                self.dfs(graph,padosi);
        
        self.stack.append(u)
            
    def transpose(self,adj,V):
        
        for i in range(V):
            for j in adj[i]:
                self.reverseGraph[j].append(i) # reversing the edge.
                
    def kosaraju(self, V, adj):
        
        self.visited =  [False for i in range(V)]
        self.stack   =  [];
        
        for i in range(V):
            
            if self.visited[i] == False:
                self.dfs(adj,i)
        
        self.transpose(adj,V);
        
        
        self.visited = [False for i in range(V)]
        result = 0
        
        while self.stack :
            
            u = self.stack.pop()
            
            if self.visited[u] == False:
                # calling with Transposed reverseGraph
                self.dfs(self.reverseGraph,u) 
                result = result + 1
            
        return result
        
        
        
 ```
