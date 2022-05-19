# https://leetcode.com/problems/combination-sum/
class Solution:
    
    def __init__(self):
        self.combn_set = []
        self.result    = []
        
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        self.helper(candidates,0,0,target)
        
        return self.result
    
    def helper(self,nums,start_index,c_sum,target):
        
        if c_sum == target:
            self.result.append(list(self.combn_set))
            return 
        
        for i in range(start_index,len(nums)):
            
            if c_sum + nums[i] <= target:
                self.combn_set.append(nums[i])
                self.helper(nums,i,c_sum+nums[i],target)
                self.combn_set.pop()
                
            # if c_sum exceeds then for loop will automatically skip over that index
            
            
            
        
        
        