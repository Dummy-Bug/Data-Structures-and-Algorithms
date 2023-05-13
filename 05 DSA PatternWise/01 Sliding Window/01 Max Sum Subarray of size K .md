### Problem Description

-> Given an array of integers Arr of size N and a number K. Return the maximum sum of a subarray of size K.

https://practice.geeksforgeeks.org/problems/max-sum-subarray-of-size-k5313/1?utm_source=gfg&utm_medium=article&utm_campaign=bottom_sticky_on_article
    


```

class Solution
{
    static long maximumSumSubarray(int K, ArrayList<Integer> Arr,int N)
    {
        int i = 0; int j = 0;
        long max_sum = 0;long curr_sum = 0;
        
        
        while ( j<Arr.size() )
        {
            curr_sum = curr_sum + Arr.get(j);
            
            if ( (j-i+1) == K )
            {
                max_sum  = Math.max(max_sum,curr_sum);
                curr_sum = curr_sum - Arr.get(i);
                j += 1; i += 1;
            }
            else
            {
                j += 1;
            }
            
            
        }
    
    return max_sum ;
    
    }

```
