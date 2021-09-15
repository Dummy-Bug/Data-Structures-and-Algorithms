class Solution:
    def LongestRepeatingSubsequence(self, str):
        
        return self.lcs(str,str,len(str),len(str))
    
    def lcs(self,string_1,string_2,len_1,len_2):
        
        dp = [[0 for i in range(len_1+1)]for j in range(len_2+1)]
        
        for i in range(1,len_2+1):
            for j in range(1,len_1+1):
                
                if i!=j and string_1[j-1] == string_2[i-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j] , dp[i][j-1])
                    
        return dp[-1][-1]