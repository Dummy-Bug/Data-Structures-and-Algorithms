# https://leetcode.com/problems/next-permutation/

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # T(c) = O(N), S(c) = O(1)
        
        BreakDownIndex = -1
        
        for i in range(len(nums)-1,0,-1):
            if nums[i] > nums[i-1]:
                
                BreakDownIndex = i-1
                break

        if BreakDownIndex != -1:
            
            for i in range(len(nums)-1,0,-1):
                
                if nums[i] > nums[BreakDownIndex]: # swap to get the bigger prefix than already present prefix
                    
                    nums[i] , nums[BreakDownIndex] = nums[BreakDownIndex], nums[i]
                    break
            
        i, j = BreakDownIndex + 1, len(nums)-1  # BreakDownIndex == -1 then it will become 0 and hence 
                                                # whole list will get reverse and that is what we want
            
        while i < j: # reverse the suffix or whole array 
            nums[i], nums[j] = nums[j], nums[i]
            i = i + 1
            j = j - 1
        
        
                    
                
                
            