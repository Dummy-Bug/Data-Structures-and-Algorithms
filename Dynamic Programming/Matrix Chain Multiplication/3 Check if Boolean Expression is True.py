class Solution:
    
    def countWays(self, N, S):
        
        return helper(S,0,N-1,True) # if we want number of ways that are true.
        
def helper(s,i,j,isTrue):
    
    if i > j :
        return False
    
    elif i == j:
        
        if isTrue:
            return s[i] == 'T'
            
        if not isTrue:
            return s[i] == 'F'
            
    ans = 0
    for k in range(i+1,j,2):
        
        lt = helper(s,i,k-1,True)# number of ways of making left equation True
        lf = helper(s,i,k-1,False)
        rt = helper(s,k+1,j,True)
        rf = helper(s,k+1,j,False)# number of ways of making right expression False
        
        if s[k] == '|':
            
            if isTrue: 
                ans = ans + lt*rf + lf*rt + lt*rt
            
            if not isTrue:
                ans = ans + lf*rf 
        
        elif s[k] == '^':
            
            if isTrue:
                ans = ans + lt*rf + lf*rt + lt*rt
                
            if not isTrue:
                ans = ans +  lf*rf
                
        else:
            
            if isTrue:
                ans = ans + lt*rt
                
            if not isTrue:
                ans = ans + lt*rf + lf*rt + lf*rf
        
    return ans