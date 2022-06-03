# https://leetcode.com/problems/range-sum-query-2d-immutable/
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.prefix_matrix = []
        
        for row in matrix:
            temp = []
            for ele in row:
                if temp == []:
                    temp.append(ele)
                else:
                    temp.append(temp[-1]+ele)
            self.prefix_matrix.append(temp)
                
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        
        result = 0
        
        for row in range(row1,row2+1):
    
            result = result + self.prefix_matrix[row][col2] - self.prefix_matrix[row][col1] + self.matrix[row][col1]
        
        return result


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)