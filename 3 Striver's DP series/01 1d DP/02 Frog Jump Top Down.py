# https://www.codingninjas.com/codestudio/problems/frog-jump_3621012?source=youtube&campaign=striver_dp_videos&utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_dp_videos&leftPanelTab=0
"""
    Time Complexity: O(N)
    Space Complexity: O(N)

    where 'N' is the number of staris in the staircase.
"""
def frogJump(n: int, heights: List[int]) -> int:
    
    dp = [None for i in range(n+1)]
    return helper(n,heights,dp)

def helper(n,heights,dp):
    if n == 1:
        return 0
    if n == 0:
        return float('inf')
    if dp[n] != None :
        return dp[n]
    
    short_jump  = abs(heights[n-1] - heights[n-2])
    longer_jump = abs(heights[n-1] - heights[n-3])
    
    dp[n] = min(short_jump + helper(n-1,heights,dp) , longer_jump + helper(n-2,heights,dp))
    return dp[n]