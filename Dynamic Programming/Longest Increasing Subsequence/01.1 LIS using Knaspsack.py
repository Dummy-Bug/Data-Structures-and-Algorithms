class Solution:
    
    def lengthOfLIS(self, nums: List[int]):
        
        
        self.temp = dict()
        
        return self.LIS(nums, 0, len(nums) ,float("-inf"))
    
    def LIS(self,nums,i,n,target):
        
        if i >= n:
            self.temp[(i,target)] = 0
            return 0
        
        if (i,target) in self.temp:
            return self.temp[(i,target)]
        
        if nums[i] > target:
            
            include = self.LIS(nums, i + 1, n, nums[i]) + 1
            
            exclude = self.LIS(nums, i + 1, n, target)
	        
            self.temp[(i,target)] =  max(include, exclude)
            
            return self.temp[(i,target)]
        else:
            self.temp[(i,target)] =  self.LIS(nums, i+1, n, target)
            
            return self.temp[(i,target)]