### Problem Description 

Given an m x n matrix, return all elements of the matrix in spiral order.

 

Example 1:


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:


Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100

```

class Solution:
    def spiralOrder(self, A: List[List[int]]) -> List[int]:
        
        start_row = start_col = 0;
        end_row   = len(A)-1;
        end_col   = len(A[0])-1;
        spiralOrder = [];
        
        while start_row <= end_row and start_col <= end_col:
            
            # Traversing the first unvisited row. 
            for j in range(start_col,end_col+1):
                spiralOrder.append(A[start_row][j]);
            
            # Traversing the last unvisited column.
            
            for i in range(start_row+1,end_row+1):
                
                spiralOrder.append(A[i][end_col]);
            
            # Traversing the last unvisited row.
            if start_row < end_row:
                for j in range(end_col-1,start_col-1,-1):

                    spiralOrder.append(A[end_row][j]);
                
            
            # Traversing the first unvisited column.
            if start_col < end_col:
                for i in range(end_row-1,start_row,-1):

                    spiralOrder.append(A[i][start_col]);
            
            start_row += 1; start_col += 1;
            end_row   -= 1; end_col   -= 1;
        
        return spiralOrder
        

```
