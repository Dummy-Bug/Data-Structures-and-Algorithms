class Solution:
    
    # TLE 
    
    def knapSack(self,W, wt, val, n):
        
        if W == 0 or n == 0:
            return 0
        
        if wt[n-1] <= W:
            
            taken     = val[n-1] + self.knapSack(W-wt[n-1], wt, val, n-1)
            not_taken = self.knapSack(W, wt, val, n-1)
            
            return max(taken,not_taken)
        else:
            return self.knapSack(W, wt, val, n-1)