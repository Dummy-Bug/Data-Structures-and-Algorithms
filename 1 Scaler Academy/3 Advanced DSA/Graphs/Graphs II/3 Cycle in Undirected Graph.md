### Problem Description

Given an undirected graph having A nodes labelled from 1 to A with M edges given in a form of matrix B of size M x 2 where (B[i][0], B[i][1]) represents two nodes B[i][0] and B[i][1] connected by an edge.

Find whether the graph contains a cycle or not, return 1 if cycle is present else return 0.

NOTE:

The cycle must contain atleast three nodes.
There are no self-loops in the graph.
There are no multiple edges between two nodes.
The graph may or may not be connected.
Nodes are numbered from 1 to A.
Your solution will run on multiple test cases. If you are using global variables make sure to clear them.


Problem Constraints

1 <= A, M <= 3*105

1 <= B[i][0], B[i][1] <= A



Input Format

The first argument given is an integer A representing the number of nodes in the graph.

The second argument given is an matrix B of size M x 2 which represents the M edges such that there is a edge between node B[i][0] and node B[i][1].



Output Format

Return 1 if cycle is present else return 0.



Example Input

Input 1:

 A = 5
 B = [  [1. 2]
        [1, 3]
        [2, 3]
        [1, 4]
        [4, 5]
     ]
Input 2:

 A = 3
 B = [  [1. 2]
        [1, 3]
     ]


Example Output

Output 1:

 1
Output 2:

 0


Example Explanation

Explanation 1:

 There is a cycle in the graph i.e 1 -> 2 -> 3 -> 1 so we will return 1
Explanation 2:

 No cycle present in the graph so we will return 0.
 
 
 **SOlution Approach**
 
 Method 1: DFS
  Like directed graphs, we can use DFS to detect cycle in an undirected graph in O(A+M) time.
  We do a DFS traversal of the given graph. For every visited vertex ‘v’, if there is an adjacent ‘u’ such that u is already visited and u is not parent of v, then there is a cycle in graph.
  If we don’t find such an adjacent for any vertex, we say that there is no cycle.
  The assumption of this approach is that there are no parallel edges between any two vertices


Method 2: Union-Find
  We can keep track of the subsets in a 1D array, let’s call it parent[].
  For each edge, make subsets using both the vertices of the edge. If both the vertices are in the same subset, a cycle is found.
  Initially, all slots of parent array are initialized to -1 (means there is only one item in every subset).
  Time Complexity: O(MlogA)
 
 
 ```
 
 class Solution:

    def solve(self, A, B):

        self.graph = dict();

        for edge in B:
            src,dst = edge;
            if src not in self.graph:
                self.graph[src] = [];
            self.graph[src].append(dst);
            if dst not in self.graph:
                self.graph[dst] = [];
            self.graph[dst].append(src);
        
        # print(self.graph)
        self.visited = set();

        for vertex in range(1,A+1):
            if vertex not in self.visited:
                if self.dfsVisit(vertex,-1):
                    return 1;
        return 0;
    
    def dfsVisit(self,vertex,parent):
        self.visited.add(vertex);
        if vertex not in self.graph:
            return False;

        for neighbor in self.graph[vertex]:
            if neighbor in self.visited:
                if parent != neighbor:
                    return True;
            else:
                if self.dfsVisit(neighbor,vertex):
                    return True;
        return False;

 
 ```
