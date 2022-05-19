# https://leetcode.com/problems/rotate-image/

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Find the Transpose , you will observe the pattern
        # just reverse the elements 
        
        i = j = 0
        n = len(matrix)
        m = len(matrix[0])
        
        while i < n:
            while j < m:
                
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]
                j = j + 1
        
            i = i + 1
            j = i
        

        i, j = 0 , 0
        
        while i < n:
            while j < m//2:
                matrix[i][j], matrix[i][m-j-1] = matrix[i][m-j-1], matrix[i][j]
                
                
                j = j + 1
            j = 0
            i = i + 1
        
        