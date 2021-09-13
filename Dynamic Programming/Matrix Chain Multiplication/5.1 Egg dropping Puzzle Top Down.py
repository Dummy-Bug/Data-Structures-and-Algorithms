class Solution:
    def eggDrop(self,n, k): 
        
        self.dp = [[-1 for j in range(k+1)]for i in range(n+1)]

        return self.helper(n,k)
        
    def helper(self,e,f):
        
        if f == 0 or f == 1:
            self.dp[e][f] =  f
            return f
        
        if e == 1:
            self.dp[e][f] = f
            return f
        
        if self.dp[e][f] != -1:
            return self.dp[e][f]
            
        result = float('inf')
        
        for k in range(1,f+1):
            
            temp  = 1 + max(self.helper(e-1,k-1) , self.helper(e,f-k) )
            
            result = min(result,temp)
        
        self.dp[e][f] =  result
        return result