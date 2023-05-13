### Problem Description 

You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

 

Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Example 3:

Input: coins = [1], amount = 0
Output: 0
 

Constraints:

1 <= coins.length <= 12
1 <= coins[i] <= 231 - 1
0 <= amount <= 104


```

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dp = [[False for j in range(amount+1)] for i in range(len(coins)+1)]
        
        output = self.helper(coins,len(coins),amount,dp)
       
        if output == float("inf"):
            return -1
        return output
        
    def helper(self,coins,n,amount,dp):
        
        if amount == 0:
            return 0
        
        if n == 0 :
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
```
