
https://leetcode.com/problems/max-area-of-island/description/

### Problem Description

You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.

 

Example 1:


Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
Output: 6
Explanation: The answer is not 11, because the island must be connected 4-directionally.
Example 2:

Input: grid = [[0,0,0,0,0,0,0,0]]
Output: 0
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 50
grid[i][j] is either 0 or 1.


**Notes**
> Just find te maximum nodes in connected component

```



class Solution:
    
    def bfs(self,grid,x,y,m,n):
        
        from collections import deque
        q = deque()
        q.append([x,y])
        count = 1
        self.visited[x][y] = True
            
        while q:
            x,y = q.popleft()
            
            for i,j in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
                
                if i>= 0 and j >= 0 and i < m and j < n:
                        
                    if self.visited[i][j] == False and grid[i][j] == 1:
                        
                        self.visited[i][j] = True
                        q.append([i,j])
                        count = count + 1
        return count
    
    def maxAreaOfIsland(self, grid: List[List[int]]):
        
        m = len(grid)
        n = len(grid[0])
        
        self.visited = [[False for i in range(n)] for j in range(m)]
        max_area = 0
        for i in range(m):
            for j in range(n):
                
                if self.visited[i][j] == False and grid[i][j] == 1:
                    area     = self.bfs(grid,i,j,m,n)
                    max_area = max(area,max_area) 
                    
        return max_area  
        
        
        ```
