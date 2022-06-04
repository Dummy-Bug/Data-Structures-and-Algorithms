# https://leetcode.com/problems/search-in-rotated-sorted-array/submissions/
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # Since one of the Subarray  will always be sorted Hence we can search for the target
        # in that Sub-Array 
        
        low = 0 ; high = len(nums)-1

        
        while low <= high:
            
            mid = (low+high)>>1 
            
            if nums[mid] == target:
                return mid
            
            if nums[low] <= nums[mid]: # This part is Sorted
                
                if nums[low] <= target <= nums[mid]: # Target lies in this SubArray
                    
                    high = mid - 1
                
                else:
                    low  = mid + 1
            
            elif nums[mid] <= nums[high]: # If this part is Sorted then do the same
                
                if nums[mid] <= target <= nums[high]:
                    
                    low = mid + 1
                
                else:
                    high = mid - 1
        
        return -1