class Solution:
    def searchInsert(self, nums, target):
        
        low, high = 0, len(nums)-1
        
        while low <= high :
            
            mid = (low+high)>>1
            
            if nums[mid] == target:
                return mid
            
            elif nums[mid] > target:
                high = mid - 1
                
            else:
                low  = mid + 1
        
        return low
                
        