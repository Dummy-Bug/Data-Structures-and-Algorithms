# https://leetcode.com/problems/max-consecutive-ones/
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        max_ones = 0
        curr_seq = 0
        for i in range(len(nums)):
            
            if nums[i] == 1:
                curr_seq += 1
            else:
                curr_seq = 0
            
            max_ones = max(max_ones,curr_seq)
        
        return max_ones
                
                
            
        