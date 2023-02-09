### Problem Description

Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

Adjacent numbers for jth number of row i is jth and (j+1)th numbers of row i+1 is



Problem Constraints
|A| <= 1000

A[i] <= 1000



Input Format
First and only argument is the vector of vector A defining the given triangle



Output Format
Return the minimum sum



Example Input
Input 1:

 
A = [ 
         [2],
        [3, 4],
       [6, 5, 7],
      [4, 1, 8, 3]
    ]
Input 2:

 A = [ [1] ]


Example Output
Output 1:

 11
Output 2:

 1


Example Explanation
Explanation 1:

 The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).
Explanation 2:

 Only 2 can be collected.
 
 
S(c) = O(M*N);

```

class Solution:
    # @param nums : list of list of integers
    # @return an integer
    def minimumTotal(self, nums):

        for row in range(1,len(nums)):
            for col in range(len(nums[row])):

                if col == 0:
                    nums[row][col] = nums[row-1][col]+nums[row][col];
                elif col == len(nums[row])-1:
                    nums[row][col] = nums[row-1][col-1]+nums[row][col];
                else:
                    nums[row][col] = min(nums[row-1][col],nums[row-1][col-1])+nums[row][col];
        # print(nums);
        return min(nums[-1]);
       

```

**Solution Approach**

For ‘top-down’ DP, starting from the node on the very top, we recursively find the minimum path sum of each node. When a path sum is calculated,
we store it in an array (memoization); the next time we need to calculate the path sum of the same node, just retrieve it from the array. However,
you will need a cache that is at least the same size as the input triangle itself to store the pathsum, which takes O(N^2) space. With some clever
thinking, it might be possible to release some of the memory that will never be used after a particular point, but the order of the nodes being 
processed is not straightforwardly seen in a recursive solution, so deciding which part of the cache to discard can be a hard job.

‘Bottom-up’ DP, on the other hand, is very straightforward: we start from the nodes on the bottom row; the min pathsums for these nodes are the
values of the nodes themselves. From there, the min pathsum at the ith node on the kth row would be the lesser of the pathsums of its two children
plus the value of itself, i.e.:

minpath[k][i] = min( minpath[k+1][i], minpath[k+1][i+1]) + triangle[k][i];

Or even better, since the row minpath[k+1] would be useless after minpath[k] is computed, we can simply set minpath as a 1D array, and iteratively update itself:

For the kth level:
minpath[i] = min( minpath[i], minpath[i+1]) + triangle[k][i];


S(c) = O(N);

```

class Solution:
    def minimumTotal(self, A):
        n = len(A)
        minimums = A[n - 1]
        for row in reversed(xrange(n - 1)):
            for col, value in enumerate(A[row]):
                minimums[col] = min(minimums[col], minimums[col + 1]) + value
        return minimums[0]

```
