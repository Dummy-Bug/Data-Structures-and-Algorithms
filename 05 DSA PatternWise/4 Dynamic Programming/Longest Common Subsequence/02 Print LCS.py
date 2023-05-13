class Solution:
    
    def LCS(self,text1,text2):

        dp = [[-1 for j in range(len(text2)+1)] for i in range(len(text1)+1) ]
        
        for i in range(len(text1)+1): # if any string is empty len(lcs) == 0
            dp[i][0] = 0 
            
        for j in range(len(text2)+1): # if any string is empty len(lcs) == 0
            dp[0][j] = 0
            
        
        for i in range(1,len(text1)+1):
            for j in range(1,len(text2)+1):
                
                if text1[i-1] == text2[j-1]:
                    dp[i][j]  =  1 + dp[i-1][j-1]
                    
                else:
                    dp[i][j]  = max(dp[i-1][j],dp[i][j-1])
        
        return self.printLCS(text1,text2,dp)
    
    def printLCS(self,x,y,dp):
        
        i, j = len(x), len(y)
        lcs = ""
        
        while i > 0 and j > 0 :
            
            if x[i-1] == y[j-1]: # if both char are same reduce both i and j
                lcs   = lcs + x[i-1]  
                i = i - 1
                j = j - 1   
            else:
                if dp[i-1][j] > dp[i][j-1]:
                    i = i -1   
                else:
                    j = j - 1
                    
        return lcs[::-1] # return the reversed string to get the final answer.  