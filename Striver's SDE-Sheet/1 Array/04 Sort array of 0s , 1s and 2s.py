# https://leetcode.com/problems/sort-colors/

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # check code studio solution to solve it in slightly different way
        low, mid, high = 0,0,len(nums)-1
        
        # only move the mid when it is pointing to the 1 else move low and high.
        while mid<= high:
            
            
            if nums[mid] == 0:
                self.swap(nums,low,mid)
                low = low + 1 # because now it has correct element in it's place
            
            if nums[mid] == 2:
                self.swap(nums,mid,high)
                high = high - 1
            else:
                mid = mid + 1
        
        
    def swap(self,nums,id1,id2):
        
        nums[id1], nums[id2] = nums[id2], nums[id1]
        