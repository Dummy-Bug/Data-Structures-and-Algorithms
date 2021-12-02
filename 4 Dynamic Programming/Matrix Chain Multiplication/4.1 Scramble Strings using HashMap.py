class Solution:
    
    def isScramble(self, s1: str, s2: str):
        
        self.dx = dict()
        
        return self.helper(s1,s2)
        
    def helper(self,s1,s2):
        
        if s1 == s2: 
            self.dx[(s1,s2)] = True
            return True
        
        if len(s1) <= 1: 
            self.dx[(s1,s2)] = False
            return False
        
        if (s1,s2) in self.dx :
            return self.dx[(s1,s2)]
        
        flag = False
        n    = len(s1)
        
        for i in range(1,n):
            
            without_swapping = self.helper(s1[0:i],s2[0:i])   and self.helper(s1[i:n],s2[i:n]) 
            
            with_swapping    = self.helper(s1[0:i],s2[n-i:n]) and self.helper(s1[i:n],s2[0:n-i]) 
            
            if without_swapping or with_swapping:
                
                flag = True
                
                break
        
        self.dx[(s1,s2)] = flag
        
        return self.dx[(s1,s2)]
                                           