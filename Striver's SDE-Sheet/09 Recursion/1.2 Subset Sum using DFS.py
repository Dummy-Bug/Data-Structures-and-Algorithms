class Solution:
    
    ### DFS ###
    
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.backtracking(res,0,[],nums)
        return res
    
    def backtracking(self,res,start,subset,nums):
        print(res)
        res.append(list(subset))
        
        for i in range(start,len(nums)):
            
            subset.append(nums[i])
            self.backtracking(res,i+1,subset,nums)
            subset.pop()
        
        