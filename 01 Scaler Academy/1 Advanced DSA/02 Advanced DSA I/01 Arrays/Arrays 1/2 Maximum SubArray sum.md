### Problem Definition

Find the contiguous non-empty subarray within an array, A of length N, with the largest sum
 
 > https://www.interviewbit.com/problems/max-sum-contiguous-subarray/ 

**Kadanes will give us maximum sum among all subarrays ending at any index i**


**Solution Approach**

Let us say Ai, Ai+1 … Aj is our optimal solution.

Note that no prefix of the solution will ever have a negative sum.

Let us say Ai … Ak prefix had a negative sum.

Sum ( Ai Ai+1 … Aj ) = Sum (Ai … Ak) + Sum(Ak+1 … Aj)

Sum ( Ai Ai+1 … Aj) - Sum(Ak+1 … Aj) = Sum(Ai … Ak)

Now, since Sum(Ai … Ak) < 0,

Sum (Ai Ai+1 … Aj) - Sum (Ak+1 … Aj) < 0

which means Sum(Ak+1 … Aj ) > Sum (Ai Ai+1 … Aj)

This contradicts the fact that Ai, Ai+1 … Aj is our optimal solution.

Instead, Ak+1, Ak+2 … Aj will be our optimal solution.

Similarly, you can prove that it is always good to include a prefix with a positive sum for the optimal solution.

Try to come up with a solution based on the previous 2 facts.

Here’s one Approach.
Keep two variables ‘curSum’ and ‘maxSum’ which denotes the current sum ending at the given position and the maximum sum of a subarray respectively.
Iterate through the array , at every index we will add the current element to our curSum , after this we can update the maxSum as max(maxSum,curSum), After this we can just check if curSum is less than 0 , if it is then just replace curSum with 0.

Time Complexity : O(n)
Space Complexity(extra) : O(1)

### Python Code

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

### Java Code


```

class Solution {
    public int maxSubArray(int[] nums) {
        int currSum = 0;
        int maxSum = Integer.MIN_VALUE;

        return getMaxSubArraySum(nums,currSum,maxSum);
    }
    private int getMaxSubArraySum(int[] nums, int currSum , int maxSum) {
        for (int currElement : nums){
            currSum += currElement;
            maxSum = Math.max(currSum , maxSum);
            if (currSum < 0){
                currSum = 0; // reset the sum
            }
        }
        return maxSum;
    }
}

```
