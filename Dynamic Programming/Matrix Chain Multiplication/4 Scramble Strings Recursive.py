class Solution:
    def isScramble(self, s1: str, s2: str):
        
        if s1 == s2: # will return True even if the strings are empty.
            return True
        
        if len(s1) <= 1: 
            return False
        
        flag = False
        n    = len(s1)
        
        for i in range(1,n):
            
            without_swapping = self.isScramble(s1[0:i],s2[0:i])   and self.isScramble(s1[i:n],s2[i:n]) 
            
            with_swapping    = self.isScramble(s1[0:i],s2[n-i:n]) and self.isScramble(s1[i:n],s2[0:n-i]) 
            
            if without_swapping or with_swapping:
                
                flag = True
                
                break
        
        return flag
                
                                                                                   
                                                                                 
        
        