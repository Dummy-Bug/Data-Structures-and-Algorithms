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

```

class Solution:
    def canFinish(self, n: int, pre: List[List[int]]):
        
          # problem is nothing but finding a cycle in directed graph
          # we can use either DFS or BFS(kahn's algo).


# let's  make the graph 
        self.graph = {i:[] for i in range(n)}    
        for edge in pre:            # edge is from b-->a, bcz it's given that we have to finish b before a.
            a, b = edge[0], edge[1] 

            self.graph[b].append(a) # appending outgoing edges of vertex b
        
        self.color = ['white' for i in range(n)]
        for i in range(n):
            if self.color[i] == 'white':
            
                if self.dfs(i) == False: # if encounter False in any of the function call return the answer 
                    return False
        return True
            
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
                

        
```
