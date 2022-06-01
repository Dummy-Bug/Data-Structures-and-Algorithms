# https://leetcode.com/problems/running-sum-of-1d-array/

'''
T(c) = O(n)
'''

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        
        
        for i in range(1,len(nums)):
            
            nums[i] = nums[i] + nums[i-1]
        
        return nums