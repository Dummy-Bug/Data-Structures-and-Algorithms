
### Find the MAX(array)-MIN(array)

### Problem Description
Given an array of integers A.

value of a array = max(array) - min(array).

Calculate and return the sum of values of all possible subarrays of A modulo 109+7.



Problem Constraints
1 <= |A| <= 100000

1 <= A[i] <= 1000000



Input Format
The first and only argument given is the integer array A.



Output Format
Return the sum of values of all possible subarrays of A modulo 109+7.



Example Input
Input 1:

 A = [1]
Input 2:

 A = [4, 7, 3, 8]


Example Output
Output 1:

 0
Output 2:

 26


Example Explanation
Explanation 1:

Only 1 subarray exists. Its value is 0.
Explanation 2:

value ( [4] ) = 4 - 4 = 0
value ( [7] ) = 7 - 7 = 0
value ( [3] ) = 3 - 3 = 0
value ( [8] ) = 8 - 8 = 0
value ( [4, 7] ) = 7 - 4 = 3
value ( [7, 3] ) = 7 - 3 = 4
value ( [3, 8] ) = 8 - 3 = 5
value ( [4, 7, 3] ) = 7 - 3 = 4
value ( [7, 3, 8] ) = 8 - 3 = 5
value ( [4, 7, 3, 8] ) = 8 - 3 = 5
sum of values % 10^9+7 = 26



**Solution Approach**

> Calculate the next greater element and previous greater element for each element in the array. Each element Ai is the maximum of all subarrays starting at (previous greater element)i + 1 to (next greater element)i - 1.

Similarly, the next smaller element and previous smaller element can be used for minimum values of subarrays

Time Complexity:- O(N)

```

from collections import deque;

class Solution:

    def solve(self, A):
        nsl = [];stack = deque([]);
        # calculating nsl 
		for i in range(len(A)):

			while stack and A[stack[-1]] >= A[i]:
				stack.pop();
			if not stack:
				nsl.append(-1);
			else:
				nsl.append(stack[-1]);
			stack.append(i);

        # calculating nsr
        nsr = [];
		stack = deque([]);

		for i in range(len(A)-1,-1,-1):

			while stack and A[stack[-1]] >= A[i]:
				stack.pop();
			if not stack:
				nsr.append(len(A));
			else:
				nsr.append(stack[-1]);
			stack.append(i);

		nsr = nsr[::-1];

        # calculating ngl
        stack = deque([]);
        ngl = [];

		for i in range(len(A)):

			while stack and A[stack[-1]] <= A[i]:
				stack.pop();
			if not stack:
				ngl.append(-1);
			else:
				ngl.append(stack[-1]);
			stack.append(i);

        # calculating ngr
        ngr = [];
		stack = deque([]);

		for i in range(len(A)-1,-1,-1):

			while stack and A[stack[-1]] <= A[i]:
				stack.pop();
			if not stack:
				ngr.append(len(A));
			else:
				ngr.append(stack[-1]);
			stack.append(i);
		ngr = ngr[::-1];

        mod = 10**9+7;
        max_contribution = min_contribution = 0;
        for i in range(len(A)):

            max_contribution += ( A[i]*(i-ngl[i])*(ngr[i]-i) )%mod
            min_contribution += ( A[i]*(i-nsl[i])*(nsr[i]-i) )%mod;

        return (max_contribution-min_contribution)%mod; 


```
