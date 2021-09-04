class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        self.max = 0
        m = len(matrix)
        n = len(matrix[0])
        
        self.path_matrix  = [[-1 for j in range(n)] for i in range(m)]
        
        for i in range(m):
            for j in range(n):
                if self.path_matrix[i][j] == -1:
                    self.dfs(matrix,i,j,m,n)
        return (1 + self.max)
        
    def dfs(self,matrix,x,y,m,n):
        
        if self.path_matrix[x][y] != -1:
            
            self.max = max(self.max, self.path_matrix[x][y] )
            return self.path_matrix[x][y]
        
        top = left = bottom = right = 0
        
        if x-1 >= 0 and matrix[x-1][y] > matrix[x][y]:
            top = 1 + self.dfs(matrix,x-1,y,m,n)
        
        if y-1 >= 0 and matrix[x][y-1] > matrix[x][y]:
            left = 1 + self.dfs(matrix,x,y-1,m,n)
        
        if x+1 < m and matrix[x+1][y] > matrix[x][y]:
            bottom = 1 + self.dfs(matrix,x+1,y,m,n)
            
        if y+1 < n and matrix[x][y+1] > matrix[x][y]:
            right = 1+ self.dfs(matrix,x,y+1,m,n)
            
        self.path_matrix[x][y] = max(top,left,bottom,right)
        self.max = max(self.max, self.path_matrix[x][y] )
        
        return self.path_matrix[x][y]
