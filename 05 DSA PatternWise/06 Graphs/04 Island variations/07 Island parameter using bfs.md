https://leetcode.com/problems/island-perimeter/description/


### Problem Description


You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

 

Example 1:


Input: grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
Output: 16
Explanation: The perimeter is the 16 yellow stripes in the image above.
Example 2:

Input: grid = [[1]]
Output: 4
Example 3:

Input: grid = [[1,0]]
Output: 4
 

Constraints:

row == grid.length
col == grid[i].length
1 <= row, col <= 100
grid[i][j] is 0 or 1.
There is exactly one island in grid.


```

class Solution:
    def islandPerimeter(self, grid: List[List[int]]):
        
        
        m = len(grid)
        n = len(grid[0])
        self.p = 0
        self.visited = [[False for j in range(n)] for i in range(m)]
        
        flag = 1
        for i in range(m):
            for j in range(n):
                if flag and grid[i][j] == 1:
                    self.bfs(grid,i,j,m,n)
                    flag = 0
        print(self.visited)
        return self.p
    
    def bfs(self,grid,x,y,m,n):
        from collections import deque
        q = deque()
        q.append([x,y])
        self.visited[x][y] = True
        
        while q:
            x,y = q.popleft()
            for i,j in [(x+1,y),(x-1,y),(x,y-1),(x,y+1)]:
                
                if i >= 0 and j >= 0 and i < m and j < n :
                    if self.visited[i][j] == False and grid[i][j] == 1:
                        self.visited[i][j] = True
                        q.append([i,j])
                    
                    elif grid[i][j] == 0:
                        self.p = self.p + 1
                else:
                    self.border(grid,i,j,m,n)
        
    def border(self,grid,x,y,m,n):
        if x < 0:
            self.p += 1
        if y < 0:
            self.p += 1
        if x > m-1:
            self.p += 1
        if y > n-1:
            self.p += 1
            
            
         ```
