class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        if sum(nums) < target:
            return 0
        s1 = sum(nums) # set1 keeping the total sum
        s2 = 0         # i will remove one element from s1 and add it to the 2nd.
        
        temp = [[-1 for j in range(sum(nums)+1)] for i in range(len(nums)+1)]
        return self.findsum(nums,len(nums),s1,s2,target,temp)
    
    def findsum(self,nums,n,s1,s2,target,dp):
    
        if n == 0:
            if s1 - s2 == target:
                return 1
            else:
                return 0
        if dp[n][s1] != -1:
            return dp[n][s1]
        
        if s1 - s2  >= target:
            
            taken     = self.findsum(nums,n-1,s1-nums[n-1],s2+nums[n-1],target,dp)
            not_taken = self.findsum(nums,n-1,s1,s2,target,dp)
        
            dp[n][s1] = taken + not_taken
            return dp[n][s1]
        else:
            dp[n][s1] =  self.findsum(nums,n-1,s1,s2,target,dp) # you can direcly return 0 here
            return dp[n][s1]
        
        
        