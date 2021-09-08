class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dp = [[float("inf") for j in range(amount+1)] for i in range(len(coins)+1)]
        
        
        
        for i in range(len(coins)+1):
            dp[i][0] = 0 # we need 0 number of coins to have 0 amount of money.
        
        for i in range(1,len(coins)+1):
            for j in range(1,amount+1):
                
                if coins[i-1] <= j:
                    
                    include  = 1 + dp[i][j-coins[i-1]]
                    
                    exclude  =     dp[i-1][j]
                    # initialized with infinity instead of -1,otherwise -1 will always be returned from min().
                    dp[i][j] = min(include,exclude) 
                
                else:
                    
                    dp[i][j] = dp[i-1][j]
        
        if dp[-1][-1] == float("inf"):
            return -1
        
        return dp[-1][-1]