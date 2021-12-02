class Solution:
    def __init__(self):
        import sys
        sys.setrecursionlimit(10**6)
    def count(self, S, m, n): 
        
        temp = [[-1 for j in range(n+1)] for i in range(m+1)]
        return self.CoinChange(S,m,n,temp)
    
    def CoinChange(self,arr,m,n,dp):
        
        if m == 0 and n > 0: # no success if we have still some cents left 
            return 0 
            
        if n == 0: # if we have zero cents left return a success 
            return 1
        if dp[m][n] != -1 :
            return dp[m][n]
            
        elif arr[m-1] <= n:
            taken     = self.CoinChange(arr,m,n-arr[m-1],dp)
            not_taken = self.CoinChange(arr,m-1,n,dp)
            
            dp[m][n]  = taken + not_taken
            return dp[m][n]
            
        else:
            dp[m][n] = self.CoinChange(arr,m-1,n,dp)
            return dp[m][n]
