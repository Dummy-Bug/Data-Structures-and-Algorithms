# https://www.codingninjas.com/codestudio/problems/frog-jump_3621012?source=youtube&campaign=striver_dp_videos&utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_dp_videos&leftPanelTab=0

def frogJump(n: int, heights) -> int:
    
    # Let's change the problem statement according to Zero indexing
    
    n = n - 1
    dp = [None for i in range(n+1)]
    
    return helper(n,heights,dp)

def helper(n,heights,dp):
    
    if n == 0: # if we are already at level 1 (0 according to zero based indexing)
        return 0
    if dp[n] != None:
        return dp[n]
    first_jump  = float('inf')
    second_jump = float('inf')
    
    first_jump = abs(heights[n] - heights[n-1] ) + helper(n-1,heights,dp) 
    
    if n > 1:
        second_jump = abs(heights[n] - heights[n-2] ) + helper(n-2,heights,dp) 
    
    dp[n] =  min(first_jump,second_jump)
    return dp[n]