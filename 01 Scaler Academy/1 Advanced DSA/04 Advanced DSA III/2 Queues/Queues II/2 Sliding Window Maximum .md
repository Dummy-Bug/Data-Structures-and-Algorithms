### Problem Description

Given an array of integers A. There is a sliding window of size B, moving from the very left of the array to the very right. 
You can only see the B numbers in the window. Each time the sliding window moves rightwards by one position. You have to find the maximum 
for each window.

Return an array C, where C[i] is the maximum value in the array from A[i] to A[i+B-1].

Refer to the given example for clarity.

NOTE: If B > length of the array, return 1 element with the max of the array.



Problem Constraints
1 <= |A|, B <= 106



Input Format
The first argument given is the integer array A.

The second argument given is the integer B.



Output Format
Return an array C, where C[i] is the maximum value of from A[i] to A[i+B-1].



Example Input
Input 1:

 A = [1, 3, -1, -3, 5, 3, 6, 7]
 B = 3
Input 2:

 A = [1, 2, 3, 4, 2, 7, 1, 3, 6]
 B = 6


Example Output
Output 1:

 [3, 3, 5, 5, 6, 7]
Output 2:

 [7, 7, 7, 7]


Example Explanation
Explanation 1:

 Window position     | Max
 --------------------|-------
 [1 3 -1] -3 5 3 6 7 | 3
 1 [3 -1 -3] 5 3 6 7 | 3
 1 3 [-1 -3 5] 3 6 7 | 5
 1 3 -1 [-3 5 3] 6 7 | 5
 1 3 -1 -3 [5 3 6] 7 | 6
 1 3 -1 -3 5 [3 6 7] | 7
Explanation 2:

 Window position     | Max
 --------------------|-------
 [1 2 3 4 2 7] 1 3 6 | 7
 1 [2 3 4 2 7 1] 3 6 | 7
 1 2 [3 4 2 7 1 3] 6 | 7
 1 2 3 [4 2 7 1 3 6] | 7

**Approach**

The double-ended queue is the perfect data structure for this problem. It supports insertion/deletion from the front and back. 
The trick is to find a way such that the largest element in the window would always appear in the front of the queue. How would you maintain 
this requirement as you push and pop elements in and out of the queue?

You might notice some redundant elements in the queue that we shouldn’t even consider about. For example, if the current queue has the elements:
[10 5 3], and a new element in the window has the element 11. Now, we could have emptied the queue without considering elements 10, 5, and 3 and 
inserted only element 11 into the queue.

A natural way most people would think is to try to maintain the queue size the same as the window’s size. Try to break away from this thought and
try to think outside of the box. Removing redundant elements and storing only elements that need to be considered in the queue is the key to 
achieving the efficient O(n) solution.


```

from collections import deque;
class Solution:

    def slidingMaximum(self, A, B):

        dq = deque(); result = [];
        i = j = 0;
        while j < len(A):

            if j-i+1 < B:
                while len(dq) != 0 and A[dq[-1]] <= A[j]:
                    dq.pop();
                dq.append(j); j += 1;

            elif j-i+1 == B:
                while len(dq) != 0 and A[dq[-1]] <= A[j]:
                    dq.pop();
                dq.append(j);
                result.append(A[dq[0]]);
                j += 1;

            elif j-i+1 > B:
                if dq[0] == i:
                    dq.popleft();
                i += 1;
            # print(dq,result)
        return result;

```
