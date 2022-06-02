# https://leetcode.com/problems/transpose-matrix/
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        
        # transposed matrix would be of size m*n and if matrix is of size n*m
        transposed_matrix = [[0 for j in range(len(matrix))] for i in range(len(matrix[0]))]
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                transposed_matrix[j][i] = matrix[i][j]
        
        return transposed_matrix
                