class Solution:
    
    def lengthOfLIS(self, nums: List[int]):
        
        result = 0
        for idx , num in enumerate(nums):
            
            ln = self.lis(nums,num,idx)
            
            result =  max(result, 1 + ln)
        
        return result
    
    def lis(self,A,target,i):
        
        if i >= len(A):
            return 0
        
        if target < A[i]:
            
            included =  1 + self.lis(A,A[i],i+1)
            
            not_included = self.lis(A,target,i+1)
            
            return max(included,not_included)
        
        else:
            
            return self.lis(A,target,i+1)
            