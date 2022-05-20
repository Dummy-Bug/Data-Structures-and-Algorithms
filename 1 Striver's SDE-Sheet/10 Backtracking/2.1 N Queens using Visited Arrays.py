# https://leetcode.com/problems/n-queens/
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        matrix = [['.'for j in range(n)]for i in range(n)]
        result = []
        
        left_row   = [1]*len(matrix)
        lower_diag = [1]*(2*len(matrix)-1)
        upper_diag = [1]*(2*len(matrix)-1)
        
        self.dfs(matrix,0,result,left_row,lower_diag,upper_diag)
        return reversed(result)
    
    def dfs(self,matrix,col,result,left_row,lower_diag,upper_diag):
        
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
            
            if self.IsSafe(matrix,row,col,left_row,lower_diag,upper_diag) :
                
                matrix[row][col] = 'Q'
                self.makeSafe_Unsafe(matrix,row,col,left_row,lower_diag,upper_diag,0)
                # increase column because we have placed one queen in it Hence no more are possible 
                self.dfs(matrix,col+1,result,left_row,lower_diag,upper_diag)
                self.makeSafe_Unsafe(matrix,row,col,left_row,lower_diag,upper_diag,1)
                # make the cells available again as we are not considering present cell for the Queen
                matrix[row][col] = '.'
    
    def IsSafe(self,matrix,row,col,left_row,lower_diag,upper_diag):
        
        n = len(matrix) - 1
        if left_row[row] and lower_diag[row+col] and upper_diag[n + (row-col)]:
            return True
    
    def makeSafe_Unsafe(self,matrix,row,col,left_row,lower_diag,upper_diag,bit):
        
        n = len(matrix) - 1
        left_row[row] = bit
        lower_diag[row+col] = bit
        upper_diag[n+(row-col)] = bit
        
