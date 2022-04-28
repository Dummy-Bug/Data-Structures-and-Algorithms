# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, nums: List[int]) -> int:
        
        max_diff  = 0 
        curr_diff = 0
        # start from back and keep on checking the difference if smaller element found 
        # take one variable that will store the maximum element so far and change 
        
        prev_max = nums[-1]
        for i in range (len(nums)-1,-1,-1):
            
            if prev_max > nums[i]:
                curr_diff = prev_max - nums[i]
            
            else:
                prev_max = nums[i]
            
            max_diff = max(max_diff,curr_diff)
        
        return max_diff
    
    # we can start from the begining as well.check the first solution submitted on leetcode.
                
                
        