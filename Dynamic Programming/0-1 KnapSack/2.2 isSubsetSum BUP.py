class Solution:
    
    def isSubsetSum (self, n, arr, sum):
        return self.subsetSum(n,arr,sum)
        
    def subsetSum(self,n,arr,sum):
        dp = [[False for i in range(sum+1)]for j in range(n+1)]
        
        for k in range(n+1):
            dp[k][0] = True # if sum == 0 , empty set will always return True
        
        for i in range(1,n+1):
            for j in range(1,sum+1):
                
                if j >= arr[i-1]:
                    included     = dp[i-1][j-arr[i-1]]
                    not_included = dp[i-1][j]
                    dp[i][j]     = included or not_included
                else:
                    dp[i][j]     = dp[i-1][j]
                    
        return dp[-1][-1]
 