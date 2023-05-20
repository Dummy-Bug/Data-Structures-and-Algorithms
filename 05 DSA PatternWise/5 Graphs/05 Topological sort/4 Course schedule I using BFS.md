https://leetcode.com/problems/course-schedule/description/

### Problem Description

There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
 

Constraints:

1 <= numCourses <= 2000
0 <= prerequisites.length <= 5000
prerequisites[i].length == 2
0 <= ai, bi < numCourses
All the pairs prerequisites[i] are unique.

**Notes**

-> can be done without seen set just keep counting the unique vertices if == n then Topo is possible


```
    
class Solution:
    
    def canFinish(self, n: int, pre: List[List[int]]):
        from collections import deque
        from collections import defaultdict

        self.seen = set()
        self.q    = deque()
        self.graph = {}
        self.in_degree = {}
        
        for edge in pre:
            u,v = edge
            
            if u not in self.graph:
                self.graph[u] = []
            self.graph[u].append(v)
            
            if v not in self.in_degree:
                self.in_degree[v] = 0
            self.in_degree[v] += 1
    
        for i in range(n):
            if i not in self.in_degree:
                self.q.append(i)
                
        self.bfs(pre)
        return ( len(self.seen)== n ) 
    
    def bfs(self,pre):
        
        while self.q:
            
            u = self.q.popleft()
            self.seen.add(u)
            
            if u not in self.graph:
                continue
                
            for padosi in self.graph[u]:
                
                if padosi not in self.seen :
                    self.in_degree[padosi] -= 1
                    
                    if self.in_degree[padosi] == 0:
                        self.q.append(padosi)
        
        
        ```
