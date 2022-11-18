### Problem Description
Given a undirected graph having A nodes. A matrix B of size M x 2 is given which represents the edges such that there is an edge between B[i][0] and B[i][1].

Find whether the given graph is bipartite or not.

A graph is bipartite if we can split it's set of nodes into two independent subsets A and B such that every edge in the graph has one node in A and another node in B

Note:

There are no self-loops in the graph.

No multiple edges between two pair of vertices.

The graph may or may not be connected.

Nodes are Numbered from 0 to A-1.

Your solution will run on multiple testcases. If you are using global variables make sure to clear them.


https://leetcode.com/problems/is-graph-bipartite/


```

class Solution:
    
    def isBipartite(self, graph: List[List[int]]) :
        
        n = len(graph)

        self.color = [-1 for i in range(n)]
        self.prev  = 0
        
        for i in range(n):
            
            if self.color[i] == -1:
                
                if self.dfs(i,graph) == False:
                    return False
                
        return True
                
                
    def dfs(self,u,graph):
        
        self.color[u] = (self.prev + 1 )%2
        
        for v in graph[u]:
            
            if self.color[v] == -1:
                
                self.prev = self.color[u]
                
                if self.dfs(v,graph) == False:
                    return False
                
            elif self.color[v] == self.color[u]:
                return False
        
        return True
            

```
