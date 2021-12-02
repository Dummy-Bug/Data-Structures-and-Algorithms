class Solution:
    
    def __init__(self):
        
        import sys
        sys.setrecursionlimit(10**6)
        
    def lcs(self,x,y,s1,s2):
        
        temp = [[-1 for j in range(len(s2)+1)] for i in range(len(s1)+1)] 
        return self.helper(x,y,s1,s2,temp)
        
    def helper(self,x,y,s1,s2,dp):
        
        if x == 0 or y == 0:
            return 0
            
        elif dp[x][y] != -1:
            return dp[x][y]
            
        elif s1[x-1] == s2[y-1]:
            
            dp[x][y] = 1 + self.helper(x-1,y-1,s1,s2,dp)
            return dp[x][y]
            
        else:
            dp[x][y] =  max( self.helper(x-1,y,s1,s2,dp),self.helper(x,y-1,s1,s2,dp) )
            
            return dp[x][y]
     