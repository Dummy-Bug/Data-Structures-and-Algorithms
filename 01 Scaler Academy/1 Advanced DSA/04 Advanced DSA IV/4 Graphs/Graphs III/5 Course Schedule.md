### Problem Description


There are a total of A courses you have to take, labeled from 1 to A.

Some courses may have prerequisites, for example to take course 2 you have to first take course 1, which is expressed as a pair: [1,2].

So you are given two integer array B and C of same size where for each i (B[i], C[i]) denotes a pair.

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

Return 1 if it is possible to finish all the courses, or 0 if it is not possible to finish all the courses.



Problem Constraints
1 <= A <= 6*104

1 <= length(B) = length(C) <= 105

1 <= B[i], C[i] <= A



Input Format
The first argument of input contains an integer A, representing the number of courses.

The second argument of input contains an integer array, B.

The third argument of input contains an integer array, C.



Output Format
Return 1 if it is possible to finish all the courses, or 0 if it is not possible to finish all the courses.



Example Input
Input 1:

 A = 3
 B = [1, 2]
 C = [2, 3]
Input 2:

 A = 2
 B = [1, 2]
 C = [2, 1]


Example Output
Output 1:

 1
Output 2:

 0


Example Explanation
Explanation 1:

 It is possible to complete the courses in the following order:
    1 -> 2 -> 3
Explanation 2:

 It is not possible to complete all the courses.
 
 
 ```
 
 class Solution:
	# @param A : integer
	# @param B : list of integers
	# @param C : list of integers
	# @return an integer
	def solve(self, n, B, C):
          # problem is nothing but finding a cycle in directed graph
          # we can use either DFS or BFS(kahn's algo).


# let's  make the graph 
        self.graph = {i:[] for i in range(1,n+1)}    
        for i in range(len(B)):
                        # edge is from b-->a, bcz it's given that we have to finish b before a.
            a, b = B[i], C[i] 

            self.graph[a].append(b) # appending outgoing edges of vertex b
        # print(self.graph);
        self.color = ['white' for i in range(n+1)]
        for i in range(1,n+1):
            if self.color[i] == 'white':
            
                if self.dfs(i) == False: # if encounter False in any of the function call return the answer 
                    return 0
        return 1
            
    def dfs(self,source):
        self.color[source] = 'grey'
        
        for padosi in self.graph[source]:
            
            if self.color[padosi] == 'grey': # if encounter unfinished edge cycle is found.
                return False                 # returning False means can't finish all the courses
            
            elif self.color[padosi] == 'white':
                if self.dfs(padosi) == False:
                    return False
        
        self.color[source] = 'black'
        return True

**Solution Approach**

Consider a graph with courses from 1 to N representing the nodes of the graph and each prerequisite pair [u, v] correspond to a directed edge from u to v.

It is obvious that we will get several disjoint components of the graph.

When is it possible for you to finish all the courses?

The problem reduces down to finding a directed cycle in the whole graph. If any such cycle is present, it is not possible to finish all the courses.

Depth First Traversal(DFS) can be used to detect cycle in a Graph. There is a cycle in a graph only if there is a back edge present in the graph. A back edge is an edge that is from a node to itself (self loop) or one of its ancestor in the tree produced by DFS.

For a disconnected graph, we can check for cycle in individual DFS trees by checking back edges.

We can use various methods for detecting a back edge. One of the method is by using the method of coloring. Assume the non-visited node are colored black, the nodes currently present in the recursion stack are colored blue and the nodes already visited and out of the recursion stack are colored grey. The edge that connects current vertex in DFS to the vertex in the recursion stack(blue coloured node) is back edge.

 
 ```
 
 ```
 
 def checkCycle(root, visited, instack, edges):
    visited[root] = True
    instack[root] = True
    ans = 0
    for node in edges[root]:
        if instack[node] == True:
            return 1
        ans |= checkCycle(node, visited, instack, edges)
    instack[root] = False
    return ans

class Solution:
    # @param A : integer
    # @param B : list of integers
    # @param C : list of integers
    # @return an integer
    def solve(self, A, B, C):
        edges = [[] for _ in range(A+1)]
        for b, c in zip(B, C):
            edges[b].append(c)

        visited = [False for _ in range(A + 1)]
        instack = [False for _ in range(A+1)]
        cycle = 0
        for i in range(1, A + 1):
            if visited[i] == False:
                cycle |= checkCycle(i, visited, instack, edges)
        return 1 - cycle
 
 ```
