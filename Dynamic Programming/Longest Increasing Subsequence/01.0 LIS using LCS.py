class Solution:
    
    def lengthOfLIS(self, nums: List[int]):
        # just sort the array and remove the duplicates then apply LCS on original array and sorted unique array.    
        arr = nums.copy()
        arr.sort()
        
        k = 0
        
        for j in range(1,len(arr)): 
            
            if arr[j] != arr[k]:
                
                arr[k+1] = arr[j]
                k = k + 1
        
        n , m = len(nums) , k + 1
        
        dp = [[-1 for j in range(m+1)] for i in range(n+1) ]
        
        for i in range(n+1): 
            dp[i][0] = 0 
            
        for j in range(m+1): 
            dp[0][j] = 0
            
        
        for i in range(1,n+1):
            for j in range(1,m+1):
                
                if nums[i-1] == arr[j-1]:
                    dp[i][j]  =  1 + dp[i-1][j-1]
                    
                else:
                    dp[i][j]  = max(dp[i-1][j],dp[i][j-1])
        
        return dp[-1][-1]
    
    # Working fine on gfg but TLE ion leetcode
    