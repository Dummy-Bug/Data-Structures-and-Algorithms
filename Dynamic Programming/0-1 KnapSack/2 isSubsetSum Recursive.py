class Solution:
    def isSubsetSum (self, n, arr, sum):
        
        if sum == 0 : # empty set has sum == 0 and hence will alwyas return True
            return True
        
        if n == 0 and sum > 0: # if set is empty and we have sum > 0 then always False
            return False
        
        elif arr[n-1] <= sum :
            
            taken     =  self.isSubsetSum(n-1,arr,sum-arr[n-1])
            not_taken =  self.isSubsetSum(n-1,arr,sum)
            
            return taken or not_taken
        else:
            return self.isSubsetSum(n-1,arr,sum)