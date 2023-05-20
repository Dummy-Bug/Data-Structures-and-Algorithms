https://leetcode.com/problems/coloring-a-border/


### Problem Description


ou are given an m x n integer matrix grid, and three integers row, col, and color. Each value in the grid represents the color of the grid square at that location.

Two squares belong to the same connected component if they have the same color and are next to each other in any of the 4 directions.

The border of a connected component is all the squares in the connected component that are either 4-directionally adjacent to a square not in the component, or on the boundary of the grid (the first or last row or column).

You should color the border of the connected component that contains the square grid[row][col] with color.

Return the final grid.

 

Example 1:

Input: grid = [[1,1],[1,2]], row = 0, col = 0, color = 3
Output: [[3,3],[3,2]]
Example 2:

Input: grid = [[1,2,2],[2,3,2]], row = 0, col = 1, color = 3
Output: [[1,3,3],[2,3,3]]
Example 3:

Input: grid = [[1,1,1],[1,1,1],[1,1,1]], row = 1, col = 1, color = 2
Output: [[2,2,2],[2,1,2],[2,2,2]]
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 50
1 <= grid[i][j], color <= 1000
0 <= row < m
0 <= col < n


```


class Solution:
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
    
        m = len(grid)
        n = len(grid[0])
        
        self.old_color = grid[row][col]
        self.new_color = color
        
        self.visited = [[False for j in range(n)] for i in range(m)]
        self.result =  [[grid[i][j] for j in range(n)] for i in range(m)]
        
        self.bfs(grid,row,col,m,n)
        return self.result
        
    def bfs(self,grid,x,y,m,n):
        
        from collections import deque
        q = deque()
        q.append([x,y])
        self.visited[x][y] == True
        
        while q:
            
            x,y = q.popleft()
            
            if self.border(x,y,m,n):
                self.result[x][y] = self.new_color
            else:
                self.connected_border(grid,x,y)
                
            for i,j in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
                
                if i >= 0 and j >= 0 and i < m and j < n :
                    
                    if self.visited[i][j] == False and grid[i][j] == self.old_color:
                        self.visited[i][j] = True
                        q.append([i,j])
                        
            
    
    def border(self,x,y,m,n):
        if x == 0 or y == 0 or x == m-1 or y == n-1:
            return True
    
    def connected_border(self,grid,x,y):

        if grid[x-1][y] == grid[x+1][y] == grid[x][y+1] == grid[x][y-1] == grid[x][y] == self.old_color :
            return
        
        self.result[x][y] = self.new_color
        
        
    ```
