class Solution:
    def lcs(self,x,y,s1,s2):
        
        if x == 0 or y == 0:
            return 0
            
        elif s1[x-1] == s2[y-1]:
            
            return 1 + self.lcs(x-1,y-1,s1,s2)
            
        else:
            return max(self.lcs(x-1,y,s1,s2),self.lcs(x,y-1,s1,s2))