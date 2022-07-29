### Sum of all Submatrices

https://www.geeksforgeeks.org/sum-of-all-submatrices-of-a-given-matrix/

**Notes**

> For each element of the matrix, let us try to find the number of sub-matrices the element will lie in. Then multiplying
that with the element and hence finding the total sum.

> Let us suppose the index of an element be (X, Y) in 0 based indexing, then the number of submatrices Sub(x,y) for this element
can be given by the formula Sub(x, y) = (X + 1) * (Y + 1) * (N – X) * (N – Y) .
This formula works because we just have to choose two different positions on the matrix that will create a submatrix that
envelopes the element. Thus, for each element, ‘sum’ can be updated as sum += Sub(x,y) * A[x][y].

> More Formally, Number of ways to choose from top-left elements (X + 1) * (Y + 1) Number of ways to choose from bottom-right elements (N - X) * (N - Y)


```

class Solution:
    
    def solve(self, A):

        result = 0;
        N = len(A);

        for i in range(N):
            for j in range(N):

                num_top_left = (i+1)*(j+1)
                num_bottom_right = (N-i)*(N-j)

                result += (num_top_left*num_bottom_right)*A[i][j];
        
        return result


```
