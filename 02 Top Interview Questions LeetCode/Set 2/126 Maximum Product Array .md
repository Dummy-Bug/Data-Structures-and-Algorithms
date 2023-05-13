### Problem Description 

Given an integer array nums, find a 
subarray
 that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

 

Example 1:

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
 

Constraints:

1 <= nums.length <= 2 * 104
-10 <= nums[i] <= 10
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

```

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxProduct(self, A):
        n = len(A)
        # store the result that is the max we have found so far
        result = A[0]
        # Max/Min stores the max/min product of
        # subarray that ends with the current number A[i]
        Max = result
        Min = result
        for i in range(1, n):
            # multiplied by a negative makes big number smaller, small number bigger
            # so we redefine the extremums by swapping them
            if A[i] < 0:
                Max, Min = Min, Max

            # max/min product for the current number is either the current number itself
            # or the max/min by the previous number times the current one
            Max = max(A[i], Max * A[i])
            Min = min(A[i], Min * A[i])

            # the newly computed max value is a candidate for our global result
            result = max(result, Max)
        return result;



```
