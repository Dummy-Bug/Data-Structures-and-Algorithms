### Problem Description 

Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.

```

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        m = len(grid)
        n = len(grid[0])		
        self.visited = [[False for j in range(n)] for i in range(m)]
		
        island_count = 0
        for i in range(m):
            for j in range(n):
		        
                if grid[i][j] == '1' and self.visited[i][j] == False :
		            
                    self.dfs(i,j,grid,m,n)
                    island_count += 1
		                       
        return island_count
		
    def dfs(self,x,y,grid,m,n):
	    
        self.visited[x][y] = True
	    
        for i,j in [(x-1,y),(x,y+1),(x+1,y),(x,y-1)] :
	        
            if i >= 0 and j >= 0 and i < m and j < n:
                if self.visited[i][j] == False and grid[i][j] == '1':
                    self.dfs(i,j,grid,m,n)

```
