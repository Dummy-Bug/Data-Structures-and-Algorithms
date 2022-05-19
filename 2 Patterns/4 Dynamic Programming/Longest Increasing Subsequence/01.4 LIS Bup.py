class Solution:
    
    def lengthOfLIS(self, nums: List[int]):
        
        dp = [0 for i in range(len(nums))]
        
        dp[0] = 1 # length of lis finishing at index 0 is 1
        
        for i in range(1,len(nums)):
            for j in range(i):
                
                if nums[j] < nums[i] and dp[j] > dp[i]: # check all LIS from j to i
                    dp[i] = dp[j]
            
            dp[i] = dp[i] + 1 # add 1 meaning adding the i'th element in the LIS
            
        return max(dp)