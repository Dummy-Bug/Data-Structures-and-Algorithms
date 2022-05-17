class Solution:
    
    ### BFS ###
    
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        output = []
        for level in range(0,len(nums)+1): # we also want Null set so starting from Zero
            
            self.backtrack(nums,0,level,[],output)
        
        return output
    
    def backtrack(self,nums,first_index,level,subset,result):
        
        if len(subset) == level:
            result.append(list(subset))
            return 
        
        for i in range(first_index,len(nums)):
            subset.append(nums[i])
            # i+1 will act as the starting index for calling function.
            self.backtrack(nums,i+1,level,subset,result)
            
            subset.pop() # now again the subset's size is reduced.
        
        