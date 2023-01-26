### Problem Description

Given an array A of N integers, find three integers in A such that the sum is closest to a given number B. Return the sum of those three integers.

Assume that there will only be one solution.



Problem Constraints
-108 <= B <= 108
1 <= N <= 104
-108 <= A[i] <= 108


Input Format
First argument is an integer array A of size N.

Second argument is an integer B denoting the sum you need to get close to.



Output Format
Return a single integer denoting the sum of three integers which is closest to B.



Example Input
Input 1:

A = [-1, 2, 1, -4]
B = 1
Input 2:

 
A = [1, 2, 3]
B = 6


Example Output
Output 1:

2
Output 2:

6


Example Explanation
Explanation 1:

 The sum that is closest to the target is 2. (-1 + 2 + 1 = 2)
Explanation 2:

 Take all elements to get exactly 6.

**Approach**
Lets sort the array.
When the array is sorted, try to fix the least integer by looping over it.
Lets say the least integer in the solution is arr[i].

Now we need to find a pair of integers j and k, such that arr[j] + arr[k] is closest to (target - arr[i]).
To do that, let us try the 2 pointer approach.
If we fix the two pointers at the end ( that is, i+1 and end of array ), we look at the sum.

If the sum is smaller than the sum we need to get to, we increase the first pointer.
If the sum is bigger, we decrease the end pointer to reduce the sum.

```

class Solution:

	def threeSumClosest(self, A, B):

        least_difference = float('inf');
        closest_sum = -1; A.sort();

        for i in range(len(A)):

            p1 = i+1;
            p2 = len(A)-1;

            while p1<p2:

                curr_sum = A[i] + A[p1] + A[p2];

                if curr_sum == B:
                    return B;
                
                if least_difference > abs(curr_sum-B):
                    least_difference = abs(curr_sum-B);
                    closest_sum = curr_sum;
                
                if curr_sum > B:
                    p2 -= 1;
                else:
                    p1 += 1;
        return closest_sum;

```
