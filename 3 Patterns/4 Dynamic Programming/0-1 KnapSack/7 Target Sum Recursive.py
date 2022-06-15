class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        if sum(nums) < target:
            return 0
        s1 = sum(nums) # set1 keeping the total sum
        s2 = 0         # i will remove one element from s1 and add it to the 2nd.
        
        return self.findsum(nums,len(nums),s1,s2,target)
    
    def findsum(self,nums,n,s1,s2,target):
    
        if n == 0:
            if s1 - s2 == target:
                return 1
            else:
                return 0
        
        if s1 - s2  >= target:
            
            taken     = self.findsum(nums,n-1,s1-nums[n-1],s2+nums[n-1],target)
            not_taken = self.findsum(nums,n-1,s1,s2,target)
        
            return taken + not_taken
        
        else:
            return  0