https://practice.geeksforgeeks.org/problems/0-1-knapsack-problem0945/1#

class Solution:
    
    def knapSack(self,W, wt, val, n):
        
        dp = [[0 for j in range(W+1)] for i in range(n+1)]
        
        for i in range(1,n+1):
            for j in range(1,W+1):
                
                if j >= wt[i-1]:
                    
                    dp[i][j] = max(val[i-1] + dp[i-1][j-wt[i-1]],dp[i-1][j])
                    
                    # just put dp array in place of recursive call 
                
                else:
                    dp[i][j] = dp[i-1][j]
                    