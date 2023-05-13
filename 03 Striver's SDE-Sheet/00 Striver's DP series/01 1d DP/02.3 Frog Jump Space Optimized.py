# https://www.codingninjas.com/codestudio/problems/frog-jump_3621012?source=youtube&campaign=striver_dp_videos&utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_dp_videos&leftPanelTab=0

  
    
def frogJump(n: int, heights: List[int]) -> int:
    
    n = n - 1
    prev1   = 0
    prev2   = 0
    second = float('inf')
    
    for i in range(1,n+1):
        
        first  = abs(heights[i] - heights[i-1]) + prev1
        if i > 1:
            second = abs(heights[i] - heights[i-2]) + prev2
        
        current = min(first,second)
        prev2  = prev1
        prev1  = current
    
    return prev1