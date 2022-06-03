# https://leetcode.com/problems/range-sum-query-2d-immutable/

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        
        self.matrix = matrix
        m,n = len(matrix),len(matrix[0])
        
        self.prefix_matrix = [[0 for j in range(n)] for i in range(m)] # Initializing prefix matrix with All zeros
        
        for i in range(m):
            for j in range(n):
                
                if i == 0 and j == 0:
                    self.prefix_matrix[i][j] = self.matrix[i][j]
                    continue
                
                if i == 0:
                    self.prefix_matrix[i][j] = self.prefix_matrix[i][j-1] + self.matrix[i][j]
                    continue
                
                if j == 0:
                    self.prefix_matrix[i][j] = self.prefix_matrix[i-1][j] + self.matrix[i][j]
                    continue
                else:
                    self.prefix_matrix[i][j] = self.prefix_matrix[i-1][j] + self.prefix_matrix[i][j-1] + self.matrix[i][j] - self.prefix_matrix[i-1][j-1]
        # print(self.prefix_matrix)
                
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        
        main_rectangle_area = self.prefix_matrix[row2][col2]
        
        if row1 == 0:
            upper_rectangle_area = 0
        else:
            upper_rectangle_area = self.prefix_matrix[row1-1][col2]
        
        if col1 == 0:
            left_rectangle_area = 0
        else:
            left_rectangle_area = self.prefix_matrix[row2][col1-1]
        
        if row1 == 0 or col1 == 0:
            left_diagonal_rectangle_area = 0
        else:
            left_diagonal_rectangle_area = self.prefix_matrix[row1-1][col1-1]
        
        # print(main_rectangle_area, left_rectangle_area ,upper_rectangle_area ,left_diagonal_rectangle_area)
        return main_rectangle_area - left_rectangle_area - upper_rectangle_area + left_diagonal_rectangle_area
        