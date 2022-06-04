# https://leetcode.com/problems/search-in-rotated-sorted-array-ii/
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        # Since one of the Subarray  will always be sorted Hence we can search for the target
        # in that Sub-Array 
 
        low = 0 ; high = len(nums)-1
 
 
        while low <= high:
            
            # Skiping the duplicates just like we did in 3 Sum
            
            while low < high and nums[low] == nums[low+1]:
                low = low + 1
            
            while high > low and nums[high] == nums[high-1]:
                high = high - 1
            
            mid = (low+high)//2
            
            # print(mid)
 
            if nums[mid] == target:
                return True
 
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
            
 
        return False
        