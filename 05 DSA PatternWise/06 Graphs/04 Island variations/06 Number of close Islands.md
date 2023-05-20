https://leetcode.com/problems/number-of-closed-islands/description/
    
### Problem Description

Given a 2D grid consists of 0s (land) and 1s (water).  An island is a maximal 4-directionally connected group of 0s and a closed island is an island totally (all left, top, right, bottom) surrounded by 1s.

Return the number of closed islands.

 

Example 1:



Input: grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
Output: 2
Explanation: 
Islands in gray are closed because they are completely surrounded by water (group of 1s).
Example 2:



Input: grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
Output: 1
Example 3:

Input: grid = [[1,1,1,1,1,1,1],
               [1,0,0,0,0,0,1],
               [1,0,1,1,1,0,1],
               [1,0,1,0,1,0,1],
               [1,0,1,1,1,0,1],
               [1,0,0,0,0,0,1],
               [1,1,1,1,1,1,1]]
Output: 2
 

Constraints:

1 <= grid.length, grid[0].length <= 100
0 <= grid[i][j] <=1



```


class Solution:
    
    def bfs(self,grid,x,y,m,n):
        
        from collections import deque
        q = deque()
        q.append([x,y])
        self.flag =  0
        self.visited[x][y] = True
            
        while q:
            x,y = q.popleft()
            
            if self.border(x,y,m,n):
                self.flag = -1
                
            for i,j in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
                
                if i>= 0 and j >= 0 and i < m and j < n:
                        
                    if self.visited[i][j] == False and grid[i][j] == 0:
                        self.visited[i][j] = True
                        q.append([i,j])
                        
                    if grid[i][j] == 0:
                        if self.border(i,j,m,n):
                            self.flag = -1
        
                        
    def border(self,i,j,m,n):
        if i == 0 or j == 0 or j == n-1 or i == m-1:
            return True
    
    def closedIsland(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])
        
        self.flag = 0
        result    = 0
        self.visited = [[False for i in range(n)] for j in range(m)]
        
        for i in range(m):
            for j in range(n):
                
                if self.visited[i][j] == False and grid[i][j] == 0:
                    self.bfs(grid,i,j,m,n)
                    result = result + 1 + self.flag 
                    
        return result 
    
    
    ```
