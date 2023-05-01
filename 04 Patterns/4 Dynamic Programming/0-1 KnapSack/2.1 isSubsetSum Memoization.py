class Solution:
    def isSubsetSum (self, N, arr, target):
       temp = [[-1 for j in range(target + 1)] for i in range(N + 1)]
       
       return self.subsetSum(arr,target,N,temp)
       
    def subsetSum(self,arr,target,n,dp):
        
        if target == 0:
            return 1
        
        if n == 0 and target > 0:
            return 0
        
        if dp[n][target] != -1:
            return dp[n][target]
        
        elif arr[n-1] <= target :
            
            taken     = self.subsetSum(arr,target-arr[n-1],n-1,dp)
            not_taken =  self.subsetSum(arr,target,n-1,dp)
            
            dp[n][target] =  (taken or not_taken)
            return dp[n][target]
            
        else:
            dp[n][target] =  self.subsetSum(arr,target,n-1,dp)
            return dp[n][target]
            