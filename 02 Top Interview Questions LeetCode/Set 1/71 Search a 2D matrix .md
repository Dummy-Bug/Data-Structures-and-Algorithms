### Problem Description 

Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
 

Example 1:


Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
Output: true
Example 2:


Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20
Output: false
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= n, m <= 300
-109 <= matrix[i][j] <= 109
All the integers in each row are sorted in ascending order.
All the integers in each column are sorted in ascending order.
-109 <= target <= 109


```

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)   - 1
        cols = len(matrix[0])- 1
        
        i = 0 # starting from top right corner 
        j = cols
        while ( i>=0 and i<= rows and j>=0 and j<=cols ):
            print(matrix[i][j])
            if matrix[i][j] == target:
                return True
            
            elif matrix[i][j] > target:
                j = j - 1
            elif matrix[i][j] < target:
                i = i + 1
        else:
            return False
```
