class Solution:
    def matrixMultiplication(self, N, arr):
        
        return self.mcm(arr,1,len(arr)-1)
        
    def mcm(self,arr,i,j):
        
        if i >= j: # array should be of length two
            return 0
            
        result = float("inf")
        
        for k in range(i,j):
            
            cost = arr[i-1]*arr[k]*arr[j]      # cost of multiplying (AB) and (CD)
            cost = cost  + self.mcm(arr,i,k)   # cost of multiplying (A) and (B)
            cost = cost  + self.mcm(arr,k+1,j) # cost of multiplying (C) and (D) 
            
            result = min(cost,result)
        
        return result
 