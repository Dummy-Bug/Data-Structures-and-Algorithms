### Problem Description 

There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].
Example 2:

Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].
Example 3:

Input: numCourses = 1, prerequisites = []
Output: [0]
 

Constraints:

1 <= numCourses <= 2000
0 <= prerequisites.length <= numCourses * (numCourses - 1)
prerequisites[i].length == 2
0 <= ai, bi < numCourses
ai != bi
All the pairs [ai, bi] are distinct.


```

class Solution:
    
    def findOrder(self, n: int, pre: List[List[int]]) -> List[int]:
     # keep on appenidng the finished nodes in queue ,if cycle is found anywhere return []
        

        self.graph = {i:[] for i in range(n)}    
        for edge in pre:            # edge is from b-->a, bcz it's given that we have to finish b before a.
            a, b = edge[0], edge[1] 

            self.graph[b].append(a) # appending outgoing edges of vertex b
        
        self.color  = ['white' for i in range(n)]
        from collections import deque
        self.result = deque() # taking queue instead of stack so that we can insert in the beginning in O(1)
                         
        for i in range(n):
            if self.color[i] == 'white':
            
                if self.dfs(i) == []: # if encounter False in any of the function call return the answer 
                    return []
        return self.result
            
    def dfs(self,source):
        self.color[source] = 'grey'
        
        for padosi in self.graph[source]:
            
            if self.color[padosi] == 'grey': # if encounter unfinished edge cycle is found.
                return []                 
            
            elif self.color[padosi] == 'white':
                if self.dfs(padosi) == []:
                    return []
        
        self.color[source] = 'black'
        self.result.appendleft(source) # O(1)
        
        return self.result
                

```
