# https://leetcode.com/problems/permutations/
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        # Think weather I can take a particular element at a particular place.

        result  = []
        self.helper(nums,[],result)
        
        return result
    
    def helper(self,nums,curr,result):
        
        if len(curr) == len(nums): # It means current_Permutation list contain all the elements
            result.append(list(curr))
            return
        
        for i in range(0,len(nums)):
            
            if nums[i] != float("inf"):
                
                curr.append(nums[i])
                original_element = nums[i]
                nums[i] = float("inf")
                self.helper(nums,curr,result)
                curr.pop()
                nums[i] = original_element
            
        
        
        