# https://leetcode.com/problems/subsets/
# T(c) = O(2^N*N) bcz Total Number of Subsets = O(2^N) and for every Subset we are appending the list.

class Solution:
    
    def __init__(self):
        self.result = []
        
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        self.helper(nums,len(nums),0,[])
        
        return self.result
    
    def helper(self,nums,N,index,curr_subset):
        
        if index >= N:
            self.result.append(list(curr_subset)) # O(n)
            # print(self.result)
            
            return
        
        curr_subset.append(nums[index])
        result = self.helper(nums,N,index+1,curr_subset)
        curr_subset.pop()
        result = self.helper(nums,N,index+1,curr_subset)