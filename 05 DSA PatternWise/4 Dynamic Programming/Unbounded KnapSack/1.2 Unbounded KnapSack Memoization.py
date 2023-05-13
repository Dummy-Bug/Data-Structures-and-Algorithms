class Solution:
    
    def __init__(self):
            import sys
            sys.setrecursionlimit(10**6)
            
    def knapSack(self, N, W, val, wt):

        temp = [[-1 for j in range(W+1)] for i in range(N+1)]
        return self.unbounded(N,W,val,wt,temp)
    
    def unbounded(self,n,w,val,wt,dp):
        if n == 0 or w <= 0:
            return 0
            
        if dp[n][w] != -1:
            return dp[n][w]
            
        elif wt[n-1] <= w:
            
            taken     = val[n-1] + self.unbounded(n,w-wt[n-1],val,wt,dp)
            not_taken = self.unbounded(n-1,w,val,wt,dp)
            dp[n][w]  = max(taken,not_taken) 
            
            return dp[n][w]
        else:
            dp[n][w]  = self.unbounded(n-1,w,val,wt,dp)    
            return dp[n][w]