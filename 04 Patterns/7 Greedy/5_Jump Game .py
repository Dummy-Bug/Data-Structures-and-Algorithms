class Solution:
    def canJump(self, nums: List[int]):
        
        last_index = len(nums) - 1
        max_index  = 0
        
        for i in range(last_index):
            
            if nums[i] == 0 and max_index <= i:
                return False
            
            max_index = max(nums[i]+i,max_index)
        
        return max_index >= last_index
        