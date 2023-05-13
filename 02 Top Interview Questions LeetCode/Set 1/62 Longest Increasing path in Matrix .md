### Problem Description 

329. Longest Increasing Path in a Matrix
Hard
7.9K
118
Companies
Given an m x n integers matrix, return the length of the longest increasing path in matrix.

From each cell, you can either move in four directions: left, right, up, or down. You may not move diagonally or move outside the boundary (i.e., wrap-around is not allowed).

 

Example 1:


Input: matrix = [[9,9,4],[6,6,8],[2,1,1]]
Output: 4
Explanation: The longest increasing path is [1, 2, 6, 9].
Example 2:


Input: matrix = [[3,4,5],[3,2,6],[2,2,1]]
Output: 4
Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.
Example 3:

Input: matrix = [[1]]
Output: 1
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 200
0 <= matrix[i][j] <= 231 - 1


```

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        self.max = 0; m = len(matrix); n = len(matrix[0])
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
        
        return self.path_matrix[x][y];
            
            
```
