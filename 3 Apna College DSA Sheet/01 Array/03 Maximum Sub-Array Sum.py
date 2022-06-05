# https://leetcode.com/problems/maximum-subarray/
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        curr_sum = max_sum = nums[0]
        
        for i in range(1,len(nums)):
            
            if curr_sum >= 0:
                curr_sum += nums[i]
            else:
                curr_sum = nums[i]
            
            max_sum = max(max_sum,curr_sum)
            
        return max_sum