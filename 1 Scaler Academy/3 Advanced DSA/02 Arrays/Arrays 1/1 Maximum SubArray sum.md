### Problem Definition

Find the contiguous non-empty subarray within an array, A of length N, with the largest sum

### Problem Constraints

- **1 <= N <= 1e6
- -1000 <= A[i] <= 1000**

### Input Format
- The first and the only argument contains an integer array, A.

### Output Format
- Return an integer representing the maximum possible sum of the contiguous subarray.

### Example Input
 A = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
 
### Example Output
Output -- 6

### Example Explanation

The subarray [4,-1,2,1] has the maximum possible sum of 6.

<br> 

### Hint 1
O(n^3) solution is simple.

You look at every pair (i,j), compute the sum of elements between i and j, and then take the maximum of the sums.

Obviously, this is not the best solution.

The next improvement is O(n^2), when you notice that you don’t need to sum up all the elements between i and j. You can add A[j] to the sum you have already calculated in the previous loop from i to j-1.

However, we are looking for something better than N^2.

For O(n) solution, can you look at the optimal subarray and deduce some observations from it?
If you start taking every element greedily, when should you stop?

### Solution Approach
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

