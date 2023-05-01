### Problem Description

Given an array A of both positive and negative integers.

Your task is to compute the sum of minimum and maximum elements of all sub-array of size B.

NOTE: Since the answer can be very large, you are required to return the sum modulo 109 + 7.



Problem Constraints
1 <= size of array A <= 105

-109 <= A[i] <= 109

1 <= B <= size of array



Input Format
The first argument denotes the integer array A.
The second argument denotes the value B



Output Format
Return an integer that denotes the required value.



Example Input
Input 1:

 A = [2, 5, -1, 7, -3, -1, -2]
 B = 4
Input 2:

 A = [2, -1, 3]
 B = 2


Example Output
Output 1:

 18
Output 2:

 3


Example Explanation
Explanation 1:

 Subarrays of size 4 are : 
    [2, 5, -1, 7],   min + max = -1 + 7 = 6
    [5, -1, 7, -3],  min + max = -3 + 7 = 4      
    [-1, 7, -3, -1], min + max = -3 + 7 = 4
    [7, -3, -1, -2], min + max = -3 + 7 = 4   
    Sum of all min & max = 6 + 4 + 4 + 4 = 18 
Explanation 2:

 Subarrays of size 2 are : 
    [2, -1],   min + max = -1 + 2 = 1
    [-1, 3],   min + max = -1 + 3 = 2
    Sum of all min & max = 1 + 2 = 3 
    
 **Approach**
 We will use Deque(Double-Ended Queue) and the concept of the sliding window.

We create two empty double-ended queues of size B (‘S’ , ‘G’) that only store indexes of elements of the current window that are not useless.
An element is useless if it can not be the maximum or minimum of the next subarrays.
-> In deque ‘G’, we maintain decreasing order of values from front to rear.
-> In deque ‘S’, we maintain increasing order of values from front to rear.

Maintain both Dequeue such that the front element gives maximum and minimum element respectively for each window.
Add that element to the sum variable.
Return the sum%10^9+7.
Note that the sum%10^9+7 will be in the range (0,10^9+6).
 
 ```
 
from collections import deque;
mod = 1000000000+7;

class Solution:

    def solve(self, A, B):

        sliding_max = self.slidingMaximum(A,B);
        sliding_min = self.slidingMinimum(A,B);

        return (sliding_max+sliding_min)%mod;


    def slidingMaximum(self, A, B):

        dq = deque(); result = 0;
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
                result = (result + A[dq[0]] )%mod;
                j += 1;

            elif j-i+1 > B:
                if dq[0] == i:
                    dq.popleft();
                i += 1;
        return result;

    def slidingMinimum(self, A, B):

        dq = deque(); result = 0;
        i = j = 0;
        while j < len(A):

            if j-i+1 < B:
                while len(dq) != 0 and A[dq[-1]] >= A[j]:
                    dq.pop();
                dq.append(j); j += 1;

            elif j-i+1 == B:
                while len(dq) != 0 and A[dq[-1]] >=A[j]:
                    dq.pop();
                dq.append(j);
                result = (result + A[dq[0]] )%mod;
                j += 1;

            elif j-i+1 > B:
                if dq[0] == i:
                    dq.popleft();
                i += 1;

        return result;

 
 ```
