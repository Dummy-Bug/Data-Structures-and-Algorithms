Problem Description
Given a matrix of integers A of size N x M consisting of 0 and 1. A group of connected 1's forms an island. From a cell (i, j) such that A[i][j] = 1 you can visit any cell that shares a corner with (i, j) and value in that cell is 1.

More formally, from any cell (i, j) if A[i][j] = 1 you can visit:

(i-1, j) if (i-1, j) is inside the matrix and A[i-1][j] = 1.
(i, j-1) if (i, j-1) is inside the matrix and A[i][j-1] = 1.
(i+1, j) if (i+1, j) is inside the matrix and A[i+1][j] = 1.
(i, j+1) if (i, j+1) is inside the matrix and A[i][j+1] = 1.
(i-1, j-1) if (i-1, j-1) is inside the matrix and A[i-1][j-1] = 1.
(i+1, j+1) if (i+1, j+1) is inside the matrix and A[i+1][j+1] = 1.
(i-1, j+1) if (i-1, j+1) is inside the matrix and A[i-1][j+1] = 1.
(i+1, j-1) if (i+1, j-1) is inside the matrix and A[i+1][j-1] = 1.
Return the number of islands.

NOTE: Rows are numbered from top to bottom and columns are numbered from left to right.



Problem Constraints
1 <= N, M <= 100

0 <= A[i] <= 1



Input Format
The only argument given is the integer matrix A.



Output Format
Return the number of islands.



Example Input
Input 1:

 A = [ 
       [0, 1, 0]
       [0, 0, 1]
       [1, 0, 0]
     ]
Input 2:

 A = [   
       [1, 1, 0, 0, 0]
       [0, 1, 0, 0, 0]
       [1, 0, 0, 1, 1]
       [0, 0, 0, 0, 0]
       [1, 0, 1, 0, 1]    
     ]


Example Output
Output 1:

 2
Output 2:

 5


Example Explanation
Explanation 1:

 The 1's at position A[0][1] and A[1][2] forms one island.
 Other is formed by A[2][0].
Explanation 2:

 There 5 island in total.
 
 
 **Solution Approach**
 -> Whenever a cell with unvisited value ‘1’ is encountered we explore all the nodes that are reachable from it and continue exploring until no more nodes are left to explore.

While exploring we mark them visited so that no nodes can be explored twice.

After completion of traversal increament the count of islands.

Find for the 1 which is not visited yet.
 
 
 ```
 
import sys;
sys.setrecursionlimit(10**9);

class Solution:

    def solve(self, matrix):
        self.visited = [[False for j in range( len(matrix[0] ))] for i in range(len(matrix))];
        # print(visited)
        num_islands = 0;
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if self.visited[i][j] == False and matrix[i][j] == 1:
                    num_islands  += 1;
                    self.dfsVisit(matrix,i,j);
        return num_islands;
        
    def dfsVisit(self,matrix,row,col):

        if matrix[row][col] == 0:
            return;
        self.visited[row][col] = True;
 
        if row-1>=0 and self.visited[row-1][col] == False:
            self.dfsVisit(matrix,row-1,col);
        if col-1>=0 and self.visited[row][col-1] == False:
            self.dfsVisit(matrix,row,col-1);
        if row+1<len(matrix) and self.visited[row+1][col] == False:
            self.dfsVisit(matrix,row+1,col);
        if col+1<len(matrix[0]) and self.visited[row][col+1] == False:
            self.dfsVisit(matrix,row,col+1);

        if row-1>=0 and col-1>=0 and self.visited[row-1][col-1] == False:
            self.dfsVisit(matrix,row-1,col-1);
        if row+1<len(matrix) and col+1 < len(matrix[0]) and self.visited[row+1][col+1] == False:
            self.dfsVisit(matrix,row+1,col+1)
        if row-1>=0 and col+1<len(matrix[0])and self.visited[row-1][col+1] == False:
            self.dfsVisit(matrix,row-1,col+1);
        if row+1<len(matrix) and col-1>=0 and self.visited[row+1][col-1] == False:
            self.dfsVisit(matrix,row+1,col-1);
 
 
 ```
