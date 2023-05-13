class Solution:
    
    def shortestCommonSupersequence(self, text1, text2, m, n):
        
        dp = [[-1 for j in range(len(text2)+1)] for i in range(len(text1)+1) ]
        
        for i in range(len(text1)+1): 
            dp[i][0] = 0 
            
        for j in range(len(text2)+1): 
            dp[0][j] = 0
            
        
        for i in range(1,len(text1)+1):
            for j in range(1,len(text2)+1):
                
                if text1[i-1] == text2[j-1]:
                    dp[i][j]  =  1 + dp[i-1][j-1]
                    
                else:
                    dp[i][j]  = max(dp[i-1][j],dp[i][j-1])
        
        # shortest would be if we subtract longest.            
        return ( len(text1) + len(text2) - dp[-1][-1] )