class Solution:
        
    def knapSack(self,W, wt, val, n):
        temp = [ [-1 for j in range(W+1)] for i in range(n+1)] 
        
        return self.kp(W,wt,val,temp,n)

    
    def kp(self,W,wt,val,dp,n):
        
        if W == 0 or n == 0:
            return 0
    
        if dp[n][W] != -1:
            return dp[n][W]
        
        elif wt[n-1] <= W:
            
            taken = val[n-1] + self.kp(W-wt[n-1], wt, val, dp, n-1)
            not_taken = self.kp(W,wt,val,dp,n-1)
            dp[n][W]   = max(taken,not_taken)
            
            return dp[n][W]
        else:
            dp[n][W] = self.kp(W,wt,val,dp,n-1)
            return dp[n][W]
