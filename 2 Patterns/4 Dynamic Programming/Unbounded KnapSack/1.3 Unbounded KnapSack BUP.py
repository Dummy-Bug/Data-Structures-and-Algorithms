class Solution:
    def knapSack(self, N, W, val, wt):

        dp = [[-1 for j in range(W+1)] for i in range(N+1)]
        
        for i in range(N+1):
            for j in range(W+1):
                
                if i == 0 or j == 0:
                    dp[i][j] = 0
                    
                elif wt[i-1] <= j:            
                    dp[i][j] = max(val[i-1] + dp[i][j-wt[i-1]] , dp[i-1][j])
                
                else:
                    dp[i][j] = dp[i-1][j]
        
        return dp[-1][-1]
