https://leetcode.com/problems/pascals-triangle/

### Problem Description 

Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


 

Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Example 2:

Input: numRows = 1
Output: [[1]]


```

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        result = []
        for i in range(0,numRows):
            new_list = [1 for j in range(i+1)] # as this will make the result array so it's size should be equal to NumRows 
            result.append(new_list)
            
        # print(result)
        
        for i in range(2,numRows): # as 0th and 1th rows are already in the desired form.
            for j in range(1,len(result[i-1])): # to get the 3rd(ith) row we have to traverse till len of 2nd(i-1) row.
                
                result[i][j] = result[i-1][j-1] + result[i-1][j]
                
        return result
        
        
```
