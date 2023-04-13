### Problem Description

A students applied for admission in IB Academy. An array of integers B is given representing the strengths of A people i.e. B[i] represents the strength of ith student.

Among the A students some of them knew each other. A matrix C of size M x 2 is given which represents relations where ith relations depicts that C[i][0] and C[i][1] knew each other.

All students who know each other are placed in one batch.

Strength of a batch is equal to sum of the strength of all the students in it.

Now the number of batches are formed are very much, it is impossible for IB to handle them. So IB set criteria for selection: All those batches having strength at least D are selected.

Find the number of batches selected.

NOTE: If student x and student y know each other, student y and z know each other then student x and student z will also know each other.



Problem Constraints

1 <= A <= 105

1 <= M <= 2*105

1 <= B[i] <= 104

1 <= C[i][0], C[i][1] <= A

1 <= D <= 109



Input Format

The first argument given is an integer A.
The second argument given is an integer array B.
The third argument given is a matrix C.
The fourth argument given is an integer D.



Output Format

Return the number of batches selected in IB.



Example Input

Input 1:

 A = 7
 B = [1, 6, 7, 2, 9, 4, 5]
 C = [  [1, 2]
        [2, 3] 
       `[5, 6]
        [5, 7]  ]
 D = 12
Input 2:

 A = 5
 B = [1, 2, 3, 4, 5]
 C = [  [1, 5]
        [2, 3]  ]
 D = 6


Example Output

Output 1:

 2
Output 2:

 1


Example Explanation

Explanation 1:

 Initial Batches :
    Batch 1 = {1, 2, 3} Batch Strength = 1 + 6 + 7 = 14
    Batch 2 = {4} Batch Strength = 2
    Batch 3 = {5, 6, 7} Batch Strength = 9 + 4 + 5 = 18
    Selected Batches are Batch 1 and Batch 2.
Explanation 2:

 Initial Batches :
    Batch 1 = {1, 5} Batch Strength = 1 + 5  = 6
    Batch 2 = {2, 3} Batch Strength = 5
    Batch 3 = {4} Batch Strength = 4  
    Selected Batch is only Batch 1.
    
  
 **Solution Approach**
 
 -> Modify the above problem in the form of an undirected weighted graph.
    Consider students as nodes and relations as edges between them.
    All connected components come under one batch.
    Strength of a batch is the sum of the weight of nodes of connected components of the graph(batch).

    After Modifying the problem statement to graph perspective, It is easy to see find the solution.

    Initiaize ans = 0

    Pick any unvisited node and find the sum of all the weights of nodes which are reachable from this node and mark all such nodes as visited. if this sum is greater than equal to D then increment ans.

    If N is the number of students and M is the number of relations then
    Time Complexity : O (N+M)

  
  ```
  
from collections import defaultdict;
import sys; 
sys.setrecursionlimit(10**9);
class Solution:
    # @param A : integer
    # @param B : list of integers
    # @param C : list of list of integers
    # @param D : integer
    # @return an integer
    def solve(self, A, B, C, D):

        self.graph   = defaultdict(list);
        self.visited = [False]*(A+1);

        for edge in C:
            src,dst = edge;
            self.graph[src].append(dst);
            self.graph[dst].append(src);
        result = 0;
        for i in range(1,A+1):
            if self.visited[i] == False:
                self.curr_sum = 0;
                group_strength = self.dfsVisit(i,B);
                # print(group_strength)
                if group_strength >= D:
                    result += 1;
        return result;
    
    def dfsVisit(self,vertex,strength_arr):
        self.visited[vertex] = True;
        self.curr_sum += strength_arr[vertex-1];

        for neighbor in self.graph[vertex]:
            if self.visited[neighbor] == False:
                self.dfsVisit(neighbor,strength_arr);
                
        return self.curr_sum;

  ```
  
  
  ```
  
  
  class DisjointSet:
    def __init__(self, n):
        self.rank = [0 for i in range(n)]
        self.parent = [i for i in range(n)]

class Solution:
    # @param A : integer
    # @param B : list of integers
    # @param C : list of list of integers
    # @param D : integer
    # @return an integer
    def solve(self, A, B, C, D):
        self.dsu = DisjointSet(A+1)
        dsu = self.dsu

        for i in range(len(C)):
            self.unionByRank(C[i][0], C[i][1])

        for i in range(1, A+1):
            dsu.parent[i] = self.findParent(i)

        strength = dict()
        batches_selected = 0

        for i in range(1, A+1):
            if dsu.parent[i] not in strength:
                strength[dsu.parent[i]] = B[i-1]
            else:
                strength[dsu.parent[i]] += B[i-1]

        for key, value in strength.items():
            if value >= D:
                batches_selected += 1
        return batches_selected

    def findParent(self, node):
        dsu = self.dsu

        if node == dsu.parent[node]:
            return node
        dsu.parent[node] = self.findParent(dsu.parent[node])
        return dsu.parent[node]

    def unionByRank(self, u, v):
        dsu = self.dsu

        parent_u = self.findParent(u)
        parent_v = self.findParent(v)

        if parent_u == parent_v:
            return
        if dsu.rank[parent_u] < dsu.rank[parent_v]:
            dsu.parent[parent_u] = parent_v
        elif dsu.rank[parent_v] < dsu.rank[parent_u]:
            dsu.parent[parent_v] = parent_u
        else:
            dsu.parent[parent_v] = parent_u
            dsu.rank[parent_u] = dsu.rank[parent_u] + 1
  
  
  ```
