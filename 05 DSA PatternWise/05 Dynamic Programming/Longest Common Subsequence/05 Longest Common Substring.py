class Solution:
    
    def longestCommonSubstr(self, s1, s2, n, m):
        
        dp = [[0 for k in range(n+1)] for l in range(m+1)]
        
        max = 0
        for i in range(m+1):
            for j in range(n+1):
                
                if i == 0 or j == 0:
                    dp[i][j] = 0
                    
                
                elif s2[i-1]==s1[j-1]:
                    
                    dp[i][j]  = 1 + dp[i-1][j-1]
                    
                    if dp[i][j] > max: 
                        max = dp[i][j]
                else: # it will reset the count hence diferentiating the code from lcs
                    dp[i][j] = 0
        return max
            