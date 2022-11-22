### Problem Description


Find largest distance Given an arbitrary unweighted rooted tree which consists of N (2 <= N <= 40000) nodes.

The goal of the problem is to find largest distance between two nodes in a tree. Distance between two nodes is a number of edges on a path between the nodes (there will be a unique path between any pair of nodes since it is a tree).

The nodes will be numbered 0 through N - 1.

The tree is given as an array A, there is an edge between nodes A[i] and i (0 <= i < N). Exactly one of the i's will have A[i] equal to -1, it will be root node.



Problem Constraints
2 <= |A| <= 40000



Input Format
First and only argument is vector A



Output Format
Return the length of the longest path



Example Input
Input 1:

 
A = [-1, 0]
Input 2:

 
A = [-1, 0, 0]


Example Output
Output 1:

 1
Output 2:

 2


Example Explanation
Explanation 1:

 Path is 0 -> 1.
Explanation 2:

 Path is 1 -> 0 -> 2.


```

import sys;
sys.setrecursionlimit(10**9);

class Solution:

    def maxDistance(self,node):

        if node not in self.graph:
            self.max_distance = max(self.max_distance,1);
            return 1;
        
        first_max = second_max = 0;
        
        for child in self.graph[node]:
            curr_val = self.maxDistance(child);
            
            if curr_val>=first_max:
                second_max = first_max;
                first_max  = curr_val;
            elif curr_val>=second_max:
                second_max = curr_val;

        self.max_distance = max(self.max_distance,first_max+second_max+1);
        return (1+first_max);

    def solve(self, A):
        
        self.max_distance = 0;
        self.graph = dict();
        
        for i in range(len(A)):
            if A[i] == -1:
                root = i
                continue;
            if A[i] not in self.graph:
                self.graph[A[i]] = [];
            self.graph[A[i]].append(i);
        
        self.maxDistance(root);
        
        return self.max_distance-1;

```


**Solution Approach**

1) pick any node u
2) find the node which is farthest from u, call it x (calculate using the same approach as in Solution 1)
3) find the node which is farthest from x, call it q (calculate using the same approach as in Solution 1)
The answer will be the length of a path from x to q.

Proof of correctness:

The crucial step is to prove that x will be one of the endpoints of the path with maximal length (note that there might be more than one such path). If it is, then the longest path from x will be the longest path in the tree.

Let d(v1, v2) be length of path between v1 and v2

Let’s prove it by contradiction: assume there is a strictly longer path between s and t, neither of which is x. Let h be a node which is closest to u among the nodes on a path between s and t. Then there are two cases:
1) h is on path between u and x

    u
    |
    |
    |
    h   x
   / \ /
  /   *
 /     \
s       t 
then d(s, t) = d(s, h) + d(h, t) <= d(s, h) + d(h, x) = d(s, x), which contradicts assumption.

2) h is not on path between u and x

    u
    |
    *---x
    |
    h
   / \
  /   \
 /     \
s       t
then

d(u, s) <= d(u, x) <= d(u, h) + d(h, x)
d(u, t) <= d(u, x) <= d(u, h) + d(h, x)

d(s, t) = d(s, h) + d(h, t)
= d(u, s) + d(u, t) - 2 d(u, h)
<= 2 d(h, x)

2 d(s, t) <= d(s, t) + 2 d(h, x)
= d(s, h) + d(h, x) + d(x, h) + d(h, t)
= d(x, s) + d(x, t)

This means that max(d(v, s), d(v, t)) >= d(s, t), which also contradicts assumption.

Thus, we proved that farthest node of a node will be one of the endpoints of the longest path.


*They hae solved it using MinHeap


```

import heapq
import resource
import sys

# Will segfault without this line.
resource.setrlimit(resource.RLIMIT_STACK, [0x10000000, resource.RLIM_INFINITY])
sys.setrecursionlimit(0x100000)

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        children = {}
        root = None
        for i, x in enumerate(A):
            if x == -1:
                root = i
            else:
                if x in children:
                    children[x] += [i]
                else:
                    children[x] = [i]
        largest_dist = 0
        for k, v in self.dfs(root, children, 0, {}).items():
            largest_dist = max(self.largest_dist_from_paths(v), largest_dist)
        return largest_dist

    def largest_dist_from_paths(self, paths):
        paths += [0, 0]
        a, b = heapq.heappop(paths), heapq.heappop(paths)
        return -1 * (a + b)

    def dfs(self, root, children, path_len, paths):
        paths[root] = [0]
        if root not in children:
            return paths
        for child in children[root]:
            paths = self.dfs(child, children, path_len + 1, paths)
            heapq.heappush(paths[root], min(paths[child]) - 1)
        return paths

```
