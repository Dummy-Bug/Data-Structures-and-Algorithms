### Problem Description
There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.

 

Example 1:


Input: m = 3, n = 7
Output: 28
Example 2:

Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down
 

Constraints:

1 <= m, n <= 100

```

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        if m == 1 and n == 1:
            return 1
        
        self.dp = [[-1 for j in range(n)] for i in range(m)]
        
        self.helper(m-1,n-1,m,n)
        return self.dp[-1][-1]
    
    def helper(self,i,j,m,n):
        
        if i < 0 or j < 0:
            return 0 
        
        if i == 0 and j == 0:
            return 1
        
        if self.dp[i][j] != -1:
            return self.dp[i][j]
        
        left  = self.helper(i-1,j,m,n)
        upper = self.helper(i,j-1,m,n)
        
        self.dp[i][j] = (left+upper)
        return self.dp[i][j]
```


**Most Optimal**

```

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        N = m+n - 2
        r = m - 1
        result = 1
        
        for i in range(1,r+1):
            result = (result*( (N-r+i)) )/i 
            
        return int(result)
```
