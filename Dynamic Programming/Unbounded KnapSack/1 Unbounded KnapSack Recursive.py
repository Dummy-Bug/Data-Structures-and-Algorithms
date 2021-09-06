class Solution:
    def knapSack(self, N, W, val, wt):
        
        return self.unbounded(N,W,val,wt)
    
    def unbounded(self,n,w,val,wt):
        if n == 0 or w == 0:
            return 0
            
        elif wt[n-1] <= w:
                     # don't reduce the size of array as we can have multiple occurences.
            taken     = val[n-1] + self.unbounded(n,w-wt[n-1],val,wt)
            not_taken = self.unbounded(n-1,w,val,wt)
            
            return max(taken,not_taken)
        
        else:
            return self.unbounded(n-1,w,val,wt) 