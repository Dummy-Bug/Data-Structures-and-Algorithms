# https://leetcode.com/problems/combination-sum-ii/
class Solution:

    def __init__(self):
        self.combn_set = []
        self.result    = []
        
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        self.helper(sorted(candidates),0,0,target)
        
        return self.result
    
    def helper(self,nums,start_index,c_sum,target):
        
        if c_sum == target:
            self.result.append(list(self.combn_set))
            return 
        
        for i in range(start_index,len(nums)):
            
            # i > start_index true means we have reached  here only if we have skipper last element and 
            # now if current element is same as that of last element then obv. we want to skip over it.
            if i != start_index and nums[i] == nums[i-1]:
                continue
            if c_sum + nums[i] <= target:
                self.combn_set.append(nums[i])
                self.helper(nums,i+1,c_sum+nums[i],target)
                self.combn_set.pop()
        