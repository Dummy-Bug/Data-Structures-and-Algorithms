### Problem Description 

Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.

 

Example 1:


Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]
Example 2:


Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
 

Constraints:

m == matrix.length
n == matrix[0].length
1 <= m, n <= 200
-231 <= matrix[i][j] <= 231 - 1
 

Follow up:

A straightforward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?


```

class Solution:
    def setZeroes(self, matrix: List[List[int]]):
        
        rows = len(matrix)
        cols = len(matrix[0])
        
        first_row = first_col = False
        
        for r in range(rows):
            if matrix[r][0] == 0:
                first_col = True
        
        for c in range(cols):
            if matrix[0][c] == 0:
                first_row = True
        
        for r in range(1,rows):
            for c in range(1,cols):
                
                if matrix[r][c] == 0:
                    matrix[r][0] = matrix[0][c] = 0
                    
        for r in range(1,rows):
            for c in range(1,cols):
                
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0
        
        # print(matrix)
        if first_row:
            for c in range(cols):
                matrix[0][c] = 0
                
        if first_col:
            for r in range(rows):
                matrix[r][0] = 0
        
```
