from typing import *

  
def frogJump(n: int, heights: List[int]) -> int:
    
    n = n - 1
    dp = [None for i in range(n+1)]
    
    if n == 0:
        return 0
    
    dp[0] = 0 # as we are already at first level
    dp[1] = abs(heights[1] - heights[0]) + dp[0]
    
    for i in range(2,n+1):
        
        first_jump  = abs(heights[i] - heights[i-1]) + dp[i-1]
        second_jump = abs(heights[i] - heights[i-2]) + dp[i-2]
        
        dp[i]  = min(first_jump,second_jump)
    
    return dp[n]