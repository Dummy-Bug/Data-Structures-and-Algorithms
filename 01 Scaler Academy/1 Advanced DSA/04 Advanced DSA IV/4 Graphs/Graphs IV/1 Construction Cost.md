### Problem Description

Given a graph with A nodes and C weighted edges. Cost of constructing the graph is the sum of weights of all the edges in the graph.

Find the minimum cost of constructing the graph by selecting some given edges such that we can reach every other node from the 1st node.

NOTE: Return the answer modulo 109+7 as the answer can be large.



Problem Constraints
1 <= A <= 100000
0 <= C <= 100000
1 <= B[i][0], B[i][1] <= N
1 <= B[i][2] <= 109



Input Format
First argument is an integer A.
Second argument is a 2-D integer array B of size C*3 denoting edges. B[i][0] and B[i][1] are connected by ith edge with weight B[i][2]



Output Format
Return an integer denoting the minimum construction cost.



Example Input
Input 1:

A = 3
B = [   [1, 2, 14]
        [2, 3, 7]
        [3, 1, 2]   ]
Input 2:

A = 3
B = [   [1, 2, 20]
        [2, 3, 17]  ]


Example Output
Output 1:

9
Output 2:

37


Example Explanation
Explanation 1:

We can take only two edges (2 -> 3 and 3 -> 1) to construct the graph. 
we can reach the 1st node from 2nd and 3rd node using only these two edges.
So, the total cost of costruction is 9.
Explanation 2:

We have to take both the given edges so that we can reach the 1st node from 2nd and 3rd node.


**Solution Approach**

-> As it can be easily be seen that the graph will not have any cyles and every other node should be rechable from the 1st.

The resulting graph is connected and without cycles. So, it will be a tree.

To minimize the cost, we can find minimum spanning tree using Kruskal or Prim algorithms.


**Prims ALgo**


```

# https://www.quora.com/Whats-the-difference-between-Prim-algorithm-and-Dijkstra-algorithm

from collections import defaultdict;
import heapq,sys;
sys.setrecursionlimit(10**9);
mod = 1000000000+7;
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
            ans = (ans+weight)%mod;
            self.visited.add(node);
            # print(weight,node)
            for neighbor in self.graph[node]:
                dst,weight = neighbor;
                heapq.heappush(heap,[weight,dst]);
        return ans;

```

**Kruskal's Algo**

```

def find(x, parent):
    if parent[x] != x:
        parent[x] = find(parent[parent[x]], parent)
    return parent[x]

def merge(x, y, parent, rank):
    px = find(x, parent)
    py = find(y, parent)
    if px == py:
        return 0
    # gfg pe dekh lena other Method se
    if rank[px] < rank[py]:
        parent[px] = py
        rank[py] += rank[px]
    else:
        parent[py] = px
        rank[px] += rank[py]
    return 1


class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return an integer
    def solve(self, A, B):
        edges = []
        for i in range(0, len(B)):
            weight = B[i][2]
            edges.append([weight, i])
        edges.sort()
        parent = []
        rank = []
        for i in range(0, A + 1):
            parent.append(i)
            rank.append(1)
        ans = 0
        Mod = 1000000007
        for x in edges:
            ind = x[1]
            val = x[0]
            u = B[ind][0]
            v = B[ind][1]
            f = merge(u, v, parent, rank)
            if f == 1:
                ans += val
                ans %= Mod
        return ans

```
