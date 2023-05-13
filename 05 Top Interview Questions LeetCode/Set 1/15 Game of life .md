https://leetcode.com/problems/game-of-life/

### Problem Description 

The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) or dead (represented by a 0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population.
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously. Given the current state of the m x n grid board, return the next state.

 

Example 1:


Input: board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]
Example 2:


Input: board = [[1,1],[1,0]]
Output: [[1,1],[1,1]]
 
 
 ```
 
 class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                
                curr_val = board[i][j];   
                live_cell_count = 0;
                    
                for x,y in [(i+1,j),(i-1,j),(i,j+1),(i,j-1),(i-1,j-1),(i+1,j-1),(i-1,j+1),(i+1,j+1)]:
                        
                    if self.isValid(x,y,board):
                        if board[x][y]%2 != 0:
                            live_cell_count += 1;
                
                if curr_val == 0 and live_cell_count == 3:
                    board[i][j] = 2;
                
                if curr_val == 1:
                    if live_cell_count < 2 or live_cell_count > 3:
                        board[i][j] = 3;
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                
                if board[i][j] == 2:
                    board[i][j] = 1;
                    
                elif board[i][j] == 3:
                    board[i][j] = 0;
    
    def isValid(self,x,y,board):
        
        if x<0 or y<0 or x>=len(board)or y>=len(board[0]):
            return False;
        else:
            return True;               
        
 
 ```
