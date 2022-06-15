# https://leetcode.com/problems/n-queens/
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        matrix = [['.'for j in range(n)]for i in range(n)]
        
        result = []
        self.dfs(matrix,0,result)
        return reversed(result)
    
    def dfs(self,matrix,col,result):
        
        if col == len(matrix[0]): # if col == n means we were able to place all queens in all columns
            
            temp_list = []
            for row in matrix:
                s = ""
                for ele in row:
                    s += ele
                temp_list.append(s)
                
            result.append(temp_list)
            return 
                
        for row in range(0,len(matrix)):
            
            if self.IsSafe(matrix,row,col) :
                
                matrix[row][col] = 'Q'
                # increase column because we have placed one queen in it Hence no more are possible 
                self.dfs(matrix,col+1,result)
                
                matrix[row][col] = '.'
    
    def IsSafe(self,matrix,row,col):
        
        curr_row = row
        curr_col = col
        
        # check for upper left diagonal
        
        while col >= 0 and row >= 0:
            
            if matrix[row][col] == 'Q':
                return False
            col -= 1
            row -= 1
        
        col = curr_col
        row = curr_row
        
        # check for left side
        
        while col >= 0:
            
            if matrix[row][col] == 'Q':
                return False
            
            col -= 1
        
        col = curr_col
        
        
        # check for lower left diagonal
        
        while col >= 0 and row < len(matrix):
            
            if matrix[row][col] == 'Q':
                return False
            
            col -= 1
            row += 1
        
        return True 
    
        
        
        
        
        
        
        
        
        
        
        