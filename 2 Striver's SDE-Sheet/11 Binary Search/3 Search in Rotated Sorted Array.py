# https://leetcode.com/problems/search-in-rotated-sorted-array/
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        ln = len(nums)
        minimum = float('inf')
        
        pivot = self.getPivot(nums)
        
        low = pivot
        hi  = pivot + ln - 1
        while low <= hi:
            mid = (low + hi)//2 
            middle = mid%ln
            if nums[middle] == target:
                return middle
            elif nums[middle] > target:
                hi = mid - 1
            else:
                low = mid + 1          
        return -1
    def getPivot(self,nums):
        low = 0
        hi  = len(nums)-1
        while low <= hi:
            mid = (low+hi)//2
            
            if nums[mid] >= nums[low] and nums[mid] <= nums[hi]:
                return low
            else: # iske andar nums[low] would be > nums[hi] always 
                if  nums[mid] > nums[hi]:
                    low = mid + 1
                
                elif nums[mid] < nums[hi]:
                    hi = mid