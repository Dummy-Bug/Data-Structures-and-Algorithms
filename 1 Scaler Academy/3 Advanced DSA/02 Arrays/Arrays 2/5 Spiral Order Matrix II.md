### Spiral Order Matrix

https://www.interviewbit.com/problems/spiral-order-matrix-ii/submissions/


**Notes**

> It's a Simple Simulation problem just do what is asked in Question 
> 

```

class Solution:

    def generateMatrix(self, A):
        
        n = A-1; m = A-1;
        
        matrix = [[0 for j in range(n+1)] for i in range(m+1)];
        num = 1;
        
        start_row = start_col = 0;
        end_row   = end_col   = n;
        
        while start_row <= end_row and start_col <= end_col:
            
            for j in range(start_col,end_col+1):
                
                matrix[start_row][j] = num
                num += 1;
            # print(matrix[start_row])
            if start_row == end_row:
                return matrix;
                
            for i in range(start_row+1,end_row+1):
                matrix[i][end_col] = num;
                num += 1;
            
            if end_col == start_col:
                return matrix;
                 
            for j in range(end_col-1,start_col-1,-1):
                matrix[end_row][j] = num
                num += 1;
            # print(matrix[end_row])
            for i in range(end_row-1,start_row,-1):
                matrix[i][start_col] = num;
                num += 1;
            
            start_row +=1 ; start_col += 1;
            end_row   -=1 ; end_col   -= 1;
        return matrix;

```
