### Problem Description 

You are given N towns (1 to N). All towns are connected via unique directed path as mentioned in the input.

Given 2 towns find whether you can reach the first town from the second without repeating any edge.

B C : query to find whether B is reachable from C.

Input contains an integer array A of size N and 2 integers B and C ( 1 <= B, C <= N ).

There exist a directed edge from A[i] to i+1 for every 1 <= i < N. Also, it's guaranteed that A[i] <= i for every 1 <= i < N.

NOTE: Array A is 0-indexed. A[0] = 1 which you can ignore as it doesn't represent any edge.



Problem Constraints
1 <= N <= 100000



Input Format
First argument is vector A

Second argument is integer B

Third argument is integer C



Output Format
Return 1 if reachable, 0 otherwise.



Example Input
Input 1:

 A = [1, 1, 2]
 B = 1
 C = 2
Input 2:

 A = [1, 1, 2]
 B = 2
 C = 1


**Solution Approach**

```

from collections import defaultdict
class Solution:
# @param A : list of integers
# @param B : integer
# @param C : integer
# @return an integer
    def solve(self, A, B, C):
            g = defaultdict(list)
            s = set()
            def dfs(node):
                if node in s:
                    return False
                s.add(node)
                if node == B:
                    return True
                for edge in g[node]:
                    if dfs(edge):
                        return True
                return False
            for index, edge in enumerate(A):
                if index == 0:
                    continue
                g[edge].append(index+1)
            return 1 if dfs(C) else 0

```
