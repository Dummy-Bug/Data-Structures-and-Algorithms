https://practice.geeksforgeeks.org/problems/articulation-point-1/1
    
Given an undirected connected graph with V vertices and adjacency list adj. You are required to find all the vertices removing which (and edges through it) disconnects the graph into 2 or more components.
Note: Indexing is zero-based i.e nodes numbering from (0 to V-1). There might be loops present in the graph.

Example 1:

Input:

Output:{1,4}
Explanation: Removing the vertex 1 will
discconect the graph as-

Removing the vertex 4 will disconnect the
graph as-

 

Your Task:
You don't need to read or print anything. Your task is to complete the function articulationPoints() which takes V and adj as input parameters and returns a list containing all the vertices removing which turn the graph into two or more disconnected components in sorted order. If there are no such vertices then returns a list containing -1.
 

Expected Time Complexity: O(V + E)
Expected Auxiliary Space: O(V)


```

from collections import defaultdict;
import sys
sys.setrecursionlimit(10**6)


class Solution:
    def __init__(self):
        self.time  = 0;
        self.AP    = set();
        
    def articulationPoints(self, n, adj):
        self.graph = adj;
        self.lowestTime      = [float("inf") for i in range(n)];
        # self.lowestTime represents lowest time in all the adjacent nodes except parent
        self.discTime = [float("inf") for i in range(n)];
        self.visited  = [False for i in range(n)];
    
        for i in range(n):
            if self.visited[i] == False:
                self.dfs(i,-1);
        return sorted(list(self.AP)) if len(self.AP)!=0 else [-1];
    
    def dfs(self,src,parent):
        self.lowestTime[src] = self.discTime[src] = self.time;
        self.time += 1;
        self.visited[src] = True;
        child = 0;

        for dst in self.graph[src]:
            if dst == parent:
                continue;
            if self.visited[dst] == False:
                self.dfs(dst,src);
                # now the dfs(v) has completed done and dusted;
                child += 1;
                self.lowestTime[src] = min(self.lowestTime[src],self.lowestTime[dst]);
                if self.lowestTime[dst] >= self.discTime[src] and parent != -1:

                    self.AP.add(src);
            else:
                self.lowestTime[src] = min(self.lowestTime[src],self.discTime[dst]);
                # we will take discTime here because what if dst node is removed
                # then src cannot be found from nodes above it etc etc.

        if parent == -1 and child>1:
            self.AP.add(src);

```
