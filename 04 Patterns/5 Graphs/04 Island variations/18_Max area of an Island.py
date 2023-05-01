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