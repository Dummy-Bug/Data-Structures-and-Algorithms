class Solution:
    def eggDrop(self,n, k):

        return self.helper(n,k)
        
    def helper(self,e,f):
        
        if f == 0 or f == 1:
            return f
        
        if e == 1:
            return f
        
        result = float('inf')
        
        for k in range(1,f+1):
            
            temp  = 1 + max(self.helper(e-1,k-1) , self.helper(e,f-k) )
            
            result = min(result,temp)
        
        return result
