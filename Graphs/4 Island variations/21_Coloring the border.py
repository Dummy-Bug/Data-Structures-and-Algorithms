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