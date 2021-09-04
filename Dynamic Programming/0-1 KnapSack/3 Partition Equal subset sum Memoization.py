class Solution:
    def equalPartition(self, N, arr):
        # problem is same as finding the subset of a given sum
        
        target = sum(arr)
        
        if target%2 != 0: # if sum is not even can't divide it into equal sum subset
            return 0
        else:
            target = target//2
            
        temp = [[-1 for j in range(target + 1)] for i in range(N + 1)]    
        return self.findsum(arr,N,target,temp) 
    
    def findsum(self,arr,n,target,dp):
        
        if target == 0:# if sum is zero then empty set will return True
            return 1
        
        if n == 0 and target > 0:# sum of an empty set can't be > 0 hence always False
            return False
        
        if dp[n][target] != -1:
            return dp[n][target]
        
        elif arr[n-1] <= target:
            
            included = self.findsum(arr,n-1,target - arr[n-1],dp)
            not_included = self.findsum(arr,n-1,target,dp)
            dp[n][target] = included or not_included
            
            return dp[n][target]
        else:
            dp[n][target] = self.findsum(arr,n-1,target,dp)
            return dp[n][target]