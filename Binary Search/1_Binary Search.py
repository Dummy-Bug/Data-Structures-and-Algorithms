class Solution:
    def search(self, nums: List[int], target: int):
        
        low,  high = 0, len(nums)-1
       
        while low <= high:
            
            mid = (low+high)>>1 
            
            if nums[mid] == target:
                return mid
            
            elif nums[mid] > target:
                high = mid - 1
                
            elif nums[mid] < target:
                low = mid + 1
        
        return -1