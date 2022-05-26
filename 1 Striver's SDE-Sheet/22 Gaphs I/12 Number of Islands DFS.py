# https://leetcode.com/problems/number-of-islands/
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