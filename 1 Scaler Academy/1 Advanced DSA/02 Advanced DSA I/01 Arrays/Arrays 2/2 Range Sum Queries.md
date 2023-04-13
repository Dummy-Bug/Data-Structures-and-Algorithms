### Sub-matrix Sum Queries

https://leetcode.com/problems/range-sum-query-2d-immutable/

**Notes**
> Leetcode has explained the solution nicely with diagrams and stuff.
>
The idea is to first create an auxiliary matrix arr[N+1][M+1] such that arr[i][j] stores sum of elements in submatrix from (0,0) to (i,j).
Once arr[][] is constructed, we can compute sum of submatrix between (x1, y1) and (x2, y2) in O(1) time.
We need to consider arr[x2][y2] and subtract all unnecessary elements.
Below is the complete expression to compute the submatrix sum in O(1) time.

Sum between (x1, y1) and (x2, y2) is,
arr[x2][y2] - arr[x2][y1-1] - arr[x1-1][y2] + arr[x1-1][y1-1]

The submatrix aux[x1-1][x2-1] is added because elements of it are subtracted twice.
Remember to return the ans%1000000007

```

class Solution:

    def solve(self, A, B, C, D, E):

        mod = 10**9 + 7

        prefix_matrix = A
#       row wise prefix_sum
        for i in range(0,len(A)):
            for j in range(1,len(A[0])):

                prefix_matrix[i][j] = (prefix_matrix[i][j-1] + A[i][j])%mod
#       column wise prefix_sum
        for i in range(1,len(A)):
            for j in range(0,len(A[0])):

                prefix_matrix[i][j] = (prefix_matrix[i-1][j] + A[i][j])%mod
        
        result = [];
        # print(prefix_matrix)

        for i in range(len(B)):
            top_row    = B[i]-1; top_col    = C[i]-1;
            bottom_row = D[i]-1; bottom_col = E[i]-1;

            query_sum = top_sum = bottom_left_sum = diagonal_sum = 0;
            # print(top_row,top_col,bottom_row,bottom_col)

            whole_sum = prefix_matrix[bottom_row][bottom_col];
            if top_row != 0:
                top_sum = prefix_matrix[top_row-1][bottom_col]
            
            if top_col != 0:
                 bottom_left_sum = prefix_matrix[bottom_row][top_col-1]
            
            if top_row != 0 and top_col != 0:
                diagonal_sum = prefix_matrix[top_row-1][top_col-1]

            # print(top_sum,bottom_left_sum,diagonal_sum)

            query_sum =  (whole_sum - ( top_sum + bottom_left_sum ) + diagonal_sum)%mod

            result.append(query_sum)
        
        return result
 

```
