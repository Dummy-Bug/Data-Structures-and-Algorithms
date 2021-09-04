class Solution:
    def canPartition(self, nums: List[int]):
        
        target = sum(nums)
        
        if target%2 != 0:
            return 0
        else:
            target = target//2
            
        dp = [[0 for i in range(target + 1)] for i in range(len(nums)+1) ]
        
        # always use base condition of recursive solution to fill 0th row and 0th column of dp matrix
        
        for i in range(len(nums)+1):
            dp[i][0] = 1 # empty has sum == 0 and hence always True
            
        for i in range(1,len(nums)+1):
            for j in range(1,target+1):
                
                if nums[i-1] <= j:
                    
                    included     = dp[i-1][j - nums[i-1]]
                    not_included = dp[i-1][j]
                    dp[i][j]     = included or not_included
                else:
                    dp[i][j]     = dp[i-1][j]
                    
        return dp[len(nums)][target]