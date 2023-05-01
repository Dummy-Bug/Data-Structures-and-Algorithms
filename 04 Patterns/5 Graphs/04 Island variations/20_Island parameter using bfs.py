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