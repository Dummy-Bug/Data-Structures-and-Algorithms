### Problem Definition

Find the contiguous non-empty subarray within an array, A of length N, with the largest sum
 
 > https://www.interviewbit.com/problems/max-sum-contiguous-subarray/ 

**Kadanes will give us maximum sum among all subarrays ending at any index i**

### Python Code:-
```
class Solution:

    def maxSubArray(self, A):

        curr_sum = 0
        max_sum  = A[0]

        for num in A:

            curr_sum += num
            max_sum   = max(curr_sum,max_sum)

            if curr_sum < 0:
                curr_sum = 0
        
        return max_sum
  ```

