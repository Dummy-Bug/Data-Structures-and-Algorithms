class Solution:
    def knapSack(self,W, wt, val, n):
        
        dp = [[0 for i in range(W+1)] for j in range(n+1)]
      
        for i in range(1,n+1):
            for j in range(1,W+1):
                
                if wt[i-1] <= j:
                    
                    taken = val[i-1]+dp[i-1][j-wt[i-1]]
                    not_taken = dp[i-1][j]
                    dp[i][j] = max(taken,not_taken)
                    
                else:
                    dp[i][j] = dp[i-1][j]
                    
        return dp[-1][-1]