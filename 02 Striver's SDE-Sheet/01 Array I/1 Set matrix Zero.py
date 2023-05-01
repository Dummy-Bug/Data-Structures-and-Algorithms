# https://leetcode.com/problems/set-matrix-zeroes/

class Solution:
    def setZeroes(self, matrix: List[List[int]]):
"""
Time Complexity: O(2*(N*M)), as we are traversing two times in a matrix,

Space Complexity: O(1)

"""
        rows = len(matrix)
        cols = len(matrix[0])
        
        first_row = first_col = False
        
        for r in range(rows): # if any zero in first row then make the flag = true
            if matrix[r][0] == 0:
                first_col = True 
        
        for c in range(cols): # if any zero in first/0'th col then make the flag = true
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
        
        if first_row:
            for c in range(cols):
                matrix[0][c] = 0
                
        if first_col:
            for r in range(rows):
                matrix[r][0] = 0
        