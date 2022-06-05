# https://leetcode.com/problems/single-element-in-a-sorted-array/
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        
        # Observation is that if every element is appearing two times then 
        # 2nd occurrence of element will always be on odd index and first on even index 
        
        low  = 0
        high = len(nums)-1
        
        while low <= high:
            
            
            mid = (low+high)>>1
            
            left  = mid - 1 if mid != 0 else None
            right = mid + 1 if mid != len(nums)-1 else None
            
            
            
            if left and right :
                if nums[left] != nums[mid] and nums[mid] != nums[right]:
                    
                    return nums[mid]
            
            elif left == None and right:
                if nums[mid] != nums[right]:
                    
                    return nums[mid]
            
            elif right == None and left:
                if nums[mid] != nums[left]:
                    
                    return nums[mid]
            
            elif  right == None and  left == None:
                
                return nums[mid]
            
            if mid%2 != 0: # If it is an odd index, compare with first occurrence.
                
                if nums[mid] == nums[mid-1]: # if order is maintained 
                    
                    low = mid + 1 # then single element will be on RHS
                
                else:
                    high = mid - 1
            
            else: # if it is an even index
                
                
                if nums[mid] == nums[mid+1]: # Compare with Last occurrence.
                    low = mid + 2

                else:
                    high = mid - 1

        
        return 'Single element does not exist'