class Solution:
    
    # https://leetcode.com/problems/subsets-ii/
    ## DfS solutions are much better options to use in such questions .
    
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        result = []
        
        self.helper(sorted(nums),0,[],result)
        return result
        
    def helper(self,nums,start_index,subset,result):
        
        
        result.append(list(subset))
        print(result)
        
        for i in range(start_index,len(nums)):
            
            if i != start_index and nums[i] == nums[i-1]:
                continue
            
            subset.append(nums[i])
            self.helper(nums,i+1,subset,result)
            subset.pop()