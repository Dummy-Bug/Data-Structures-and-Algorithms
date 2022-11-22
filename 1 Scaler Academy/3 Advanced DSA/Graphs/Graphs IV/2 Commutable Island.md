
**Solution Approach**

We can assume islands as the vertex points and bridges as the edges and can construct a graph with the the help of them. After constructing the graph, the problem boils down to finding a subset of edges which helps in connecting vertices in a single connected component such that the sum of their edge weights is as minimum as possible.

Now since the problem is clear to you, can you think of any graph theory algorithms related to this?

Well the answer to this problem is the classic minimum spanning tree algorithm. In this algorithm we aim at finding subset of the edges of a connected, edge-weighted undirected graph that connects all the vertices together, without any cycles and with the minimum possible total edge weight.

There are many algorithms for finding minimum spanning tree of a graph. Some of them are Kruskal’s algorithm, Prim’s algorithm etc.

Kruskal’s algorithm in detail can be found at : https://en.wikipedia.org/wiki/Kruskal%27s_algorithm
Prim’s algorithm in detail can be found at : https://en.wikipedia.org/wiki/Prim%27s_algorithm

Now, can you code this?

```

# https://www.quora.com/Whats-the-difference-between-Prim-algorithm-and-Dijkstra-algorithm

from collections import defaultdict;
import heapq,sys;
sys.setrecursionlimit(10**9);

class Solution:

    def solve(self, A, B):
        self.graph = defaultdict(list);

        for edge in B:
            src,dst,wt = edge;
            self.graph[src].append([dst,wt]);
            self.graph[dst].append([src,wt]);
        
        # print(self.graph);

        self.visited = set();
        return self.primsAlgo(1);
    
    def primsAlgo(self,node):
        ans  = 0; 
        heap = [];
        heapq.heappush(heap,[0,node]);

        while len(heap)>0:

            weight , node = heapq.heappop(heap);
            if node in self.visited:
                continue;
            ans = ans+weight ;
            self.visited.add(node);
            # print(weight,node)
            for neighbor in self.graph[node]:
                dst,weight = neighbor;
                heapq.heappush(heap,[weight,dst]);
        return ans;


```
