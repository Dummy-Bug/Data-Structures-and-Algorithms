# https://leetcode.com/problems/permutations/
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        # Think weather I can take a particular element at a particular place.
        
        visited = [False for i in range(len(nums))]
        result  = []
        self.helper(nums,[],result,visited)
        
        return result
    
    def helper(self,nums,curr,result,visited):
        
        if len(curr) == len(nums): # It means current_Permutation list contain all the elements
            result.append(list(curr))
            return
        
        for i in range(0,len(nums)):
            
            if not visited[i]:
                
                visited[i] = True
                curr.append(nums[i])
                self.helper(nums,curr,result,visited)
                curr.pop()
                visited[i] = False
            
        
        
        