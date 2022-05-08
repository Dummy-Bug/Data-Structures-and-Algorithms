# https://leetcode.com/problems/unique-paths/
# T(C) = O(m*n), S(C) = O(M*N)
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

# T(C) -- (m)

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        N = m+n - 2
        r = m - 1
        result = 1
        
        for i in range(1,r+1):
            result = (result*( (N-r+i)) )/i 
            
        return int(result)