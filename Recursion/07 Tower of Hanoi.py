class Solution:
    def shiftPile(self, N, n):
        
        if N == 1:
            return (1,3)
        else:
            self.count = 0
            self.ans   = []
            self.solve(N,n,1,3,2)
            
            return self.ans
    
    def solve(self,N,n,src,dst,helper):
        
        if N == 1:
            
            self.count = self.count + 1
            
            if self.count == n:
                self.ans = [str(src),str(dst)]
            return
        
        self.solve(N-1,n,src,helper,dst)
    
        self.count = self.count + 1
        if self.count == n:
                self.ans = [str(src),str(dst)]
        
        self.solve(N-1,n,helper,dst,src)