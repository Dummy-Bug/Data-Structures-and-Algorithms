class Solution:
    def count(self, S, m, n): 
        
        dp = [[-1 for j in range(n+1)] for i in range(m+1)]
  
        # fill the matrix according to base conditions of recursive solution.
        for j in range(n+1):  
            dp[0][j] = 0           
  
        for i in range(m+1):# (0,0) should be 1 hence don't change the order
            dp[i][0] = 1    # of base conditions 
            
   
        for i in range(1,m+1):
            for j in range(1,n+1):
                
                if S[i-1] <= j:
                    dp[i][j] = dp[i][j-S[i-1]] + dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]
       
        return dp[m][n]
