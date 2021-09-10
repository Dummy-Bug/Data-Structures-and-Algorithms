class Solution:
    
    def minCut(self, s: str) -> int:
        
        return helper(s,0,len(s)-1)

def helper(s,i,j):
    
    if i >= j :
        return 0 
    
    if check(s,i,j):
        return 0
     
    mincuts = float("inf")
    
    for k in range(i,j):
        
        cuts = 1
        cuts = cuts + helper(s,i,k)
        cuts = cuts + helper(s,k+1,j)
        
        mincuts = min(cuts,mincuts)
    
    return mincuts
        
        
        
def check(s,i,j):
    
    while i < j:
        
        if s[i] != s[j]:
            return 0
        
        i = i + 1
        j = j - 1
        
    return 1