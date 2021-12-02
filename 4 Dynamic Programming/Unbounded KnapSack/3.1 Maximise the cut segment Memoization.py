class Solution:
    def __init__(self):
        
        import sys
        sys.setrecursionlimit(10**6)
        
    def maximizeTheCuts(self,amount,x,y,z):
        
        coins = [x,y,z]
        dp = [[False for j in range(amount+1)] for i in range(len(coins)+1)]
        
        output = self.helper(coins,len(coins),amount,dp)
        
        if output == float("-inf"):
            return 0
        return output
        
    def helper(self,coins,n,amount,dp):
        
        if amount == 0:
            return 0
        
        if n == 0 : 
        # returning the smalles possible number so that max()always ignore it.
            return float("-inf")
        
        if dp[n][amount] != False: 
            return dp[n][amount]
        
        if coins[n-1] <= amount :
            
            include = 1 + self.helper(coins,n,amount-coins[n-1],dp)
            exclude = self.helper(coins,n-1,amount,dp)
            
            dp[n][amount] = max(include,exclude)
            
            return dp[n][amount]
        else:
            dp[n][amount] = self.helper(coins,n-1,amount,dp)
            
            return dp[n][amount]