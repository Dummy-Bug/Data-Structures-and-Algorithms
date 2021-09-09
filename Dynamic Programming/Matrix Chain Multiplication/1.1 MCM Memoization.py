class Solution:
    def matrixMultiplication(self, N, arr):
        
        temp = [[False for j in range(N+1)] for i in range(N+1)]
        
        return self.mcm(arr,1,len(arr)-1,temp)
        
    def mcm(self,arr,i,j,dp):
        
        if i >= j: # array should be of length two
            return 0
        
        if dp[i][j] != False:
            return dp[i][j]
            
        result = float("inf")
        
        for k in range(i,j):
            
            cost = arr[i-1]*arr[k]*arr[j]         # cost of multiplying (AB) and (CD)
            cost = cost  + self.mcm(arr,i,k,dp)   # cost of multiplying (A) and (B)
            cost = cost  + self.mcm(arr,k+1,j,dp) # cost of multiplying (C) and (D) 
            
            result = min(cost,result)
            
            dp[i][j] = result
            
        return dp[i][j]