### Rotate the image by 90 degree

https://leetcode.com/problems/rotate-image/

Let’s say our matrix is,

        * * * ^ * * *
        * * * | * * *
        * * * | * * *
        * * * | * * *
After rotating right, it appears (observe arrow direction)

        * * * *
        * * * *
        * * * *
        -- - - >
        * * * *
        * * * *
        * * * *
The idea is simple. Transform each row of the source matrix into the required column of the final matrix.

From the above picture, we can observe that.

first row of source ------> last column of destination
second row of source ------> last but-one column of destination
so ... on

last row of source ------> first column of destination
Thus, if we were allowed extra memory, the solution should be easy.

    result[j][matrix.size() - i - 1] = matrix[i][j];
    
## Approach 1 
> Using Transpose of Matrix

```

class Solution:
    
    def solve(self, A):
        
        # Finding the Transpose of the matrix;
        n = m = len(A);
        for i in range(n):
            for j in range(i+1,m):

                A[i][j],A[j][i] = A[j][i],A[i][j]

        i = 0; j = n-1;
        
        for col in range(m//2):

            for row in range(n):

                A[row][col], A[row][m-col-1] = A[row][m-col-1],A[row][col]
                
 ```
 
       
 ### Approach 2
 
 Original Matrix
                       [
                        1 2 3
                        4 5 6
                        7 8 9
                        ]
 Rotated Matrix
  
                      [
                        7 4 1
                        8 5 2
                        9 6 3
                      ]
 
 **Notes**
 
 > If you notice, if you read out the column ‘i’ in reverse order, it corresponds to the new row ‘i’ in the resulting array. So, column 0 in the original array read out in reverse order is 7 4 1, which is row 0 in answer. And so on. So you just simulate this approach and keep creating the result in another 2 D array.

However, this approach requires additional space of O(n^2) where n = number of rows in a 2D array.

Now let’s say we have to do things in place ( no extra space allowed ). This implies that we have to make things work by just moving elements around with constant extra memory.
So, let’s try to observe where elements need to end up in the result array.

* 7 needs to end up in 1's position. 
* If 7 goes to 1's position, then we need to check where 1 needs to go otherwise, value 1 will be lost. 1 needs to go to 3's position. 
* 3 needs to go to 9's position. 
* 9 needs to go to 7's position. 
* We already have placed 7 in 1's position. 
So when we move these 4 elements, all 4 elements are in their correct position.

Let’s look at 4 now.

4 -> 2 -> 6 -> 8. 
Again, a group of 4. So, we can move these elements group by group without requiring creating a copy of the array.

You can try a few more examples to convince yourself.

The code just tries to simulate what’s being discussed here.

```

class Solution:
    
    def solve(self, matrix):
        
        m = n = len(matrix)-1;
        
        for row in range((m+1)//2):
            
            for col in range(row,n-row):
                
                temp = matrix[row][col];
                
                matrix[row][col]     = matrix[m-col][row];
                matrix[m-col][row]   = matrix[m-row][n-col];
                matrix[m-row][n-col] = matrix[col][n-row]
                
                matrix[col][n-row]   = temp;
                
```
