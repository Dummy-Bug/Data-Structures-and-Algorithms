# https://leetcode.com/problems/sudoku-solver/
class Solution:
    
  
    def solveSudoku(self, board: List[List[str]]) -> None:
        
        self.helper(board)

        
    
    def helper(self,board):
    
        for i in range(9):
            for j in range(9):

                if board[i][j] == ".":
                    
                    for num in range(1,10):
                        
                        if self.IsSafe(str(num),board,i,j):
                            
                            board[i][j] = str(num)
                            
                            if self.helper(board):
                                return True  #bcz we just want only one answer so if we have got that 
                                             # then just return 
                            else:
                                board[i][j] = '.'
                    else: # if we have tried all number from 1 to 9 and could not fill the cell then
                      # it means we cannot 
                        
                        return False

        return True # if we have traversed the entire board then return True 
    
    def IsSafe(self,num,board,row,col):

        for i in range(0,9):
            
            if board[i][col] == num:
                # print("Col already contains",num)
                return False
            
            if board[row][i] == num:
                # print("Row already contains",num)
                return False
            
            # row//3 gives us the row_wise block number , 3 is the size of each block
            # thus 3*row//3 gives us the first row of the desired block
            # then we take help of 3*col//3 to get the required block col wise
            if board[3*(row//3)+i//3][3*(col//3)+i%3] == num:
                return False
        
        return True
                            
                