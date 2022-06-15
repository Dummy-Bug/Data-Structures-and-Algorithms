# https://practice.geeksforgeeks.org/problems/subset-sum-problem-1611555638/1/#

class Solution:
    
    def isSubsetSum (self, N, arr, sum):
        
        
        dp = [[0 for j in range(sum+1)]for i in range(N+1)]
        
        
        # Here i have just ignored the initialization condition and used extra condition
        # of arr[i-1] == j, if we have found the sum then return 1 from there itself no need of subtracting it and making it zero
        # and then returning zero but earlier approaches are more intuitive
        for i in range(1,N+1):
            for j in range(1,sum+1):
                
                if arr[i-1] < j:
                    
                    dp[i][j] = (dp[i-1][ j-arr[i-1] ]) or (dp[i-1][j])
                
                elif arr[i-1] == j:
                    dp[i][j]  = 1
                    
                else:
                    dp[i][j] = dp[i-1][j]
                    
        return dp[N][sum]