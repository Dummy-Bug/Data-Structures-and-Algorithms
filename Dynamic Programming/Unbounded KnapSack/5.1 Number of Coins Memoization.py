class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dp = [[False for j in range(amount+1)] for i in range(len(coins)+1)]
        
        output = self.helper(coins,len(coins),amount,dp)
       
        if output == float("inf"):
            return -1
        return output
        
    def helper(self,coins,n,amount,dp):
        
        if amount == 0:# filling the 0th column of the matrix
            return 0
        
        if n == 0 : # filling the 0th row of the matrix
            return float("inf")
        
        if dp[n][amount] != False: 
            return dp[n][amount]
        
        if coins[n-1] <= amount :
            
            include = 1 + self.helper(coins,n,amount-coins[n-1],dp)
            exclude = self.helper(coins,n-1,amount,dp)
            
            dp[n][amount] = min(include,exclude)
            
            return dp[n][amount]
        else:
            dp[n][amount] = self.helper(coins,n-1,amount,dp)
            
            return dp[n][amount]