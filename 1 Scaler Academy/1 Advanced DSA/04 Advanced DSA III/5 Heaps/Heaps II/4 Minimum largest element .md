### Problem Description

Given an array A of N numbers, you have to perform B operations. In each operation, you have to pick any one of the N elements and add the 
original value(value stored at the index before we did any operations) to its current value. You can choose any of the N elements in each 
operation.

Perform B operations in such a way that the largest element of the modified array(after B operations) is minimized.
Find the minimum possible largest element after B operations.



Problem Constraints
1 <= N <= 106
0 <= B <= 105
-105 <= A[i] <= 105



Input Format
The first argument is an integer array A.
The second argument is an integer B.



Output Format
Return an integer denoting the minimum possible largest element after B operations.



Example Input
Input 1:

 A = [1, 2, 3, 4] 
 B = 3
Input 2:

 A = [5, 1, 4, 2] 
 B = 5


Example Output
Output 1:

 4
Output 2:

 5


Example Explanation
Explanation 1:

 Apply operation on element at index 0, the array would change to [2, 2, 3, 4]
 Apply operation on element at index 0, the array would change to [3, 2, 3, 4]
 Apply operation on element at index 0, the array would change to [4, 2, 3, 4]
 Minimum possible largest element after 3 operations is 4.
Explanation 2:

 Apply operation on element at index 1, the array would change to [5, 2, 4, 2]
 Apply operation on element at index 1, the array would change to [5, 3, 4, 2]
 Apply operation on element at index 1, the array would change to [5, 4, 4, 2]
 Apply operation on element at index 1, the array would change to [5, 5, 4, 2]
 Apply operation on element at index 3, the array would change to [5, 5, 4, 4]
 Minimum possible largest element after 5 operations is 5.
 
 **Approach**
 
 Let’s keep a state array to keep track of the value of every element in the array after K operations.
Maintain a state array, which tells about the state of the array after every operation.
Initially, the state array will be the same as the initial array.

We need to consider the next state of every element in the array.
Consider a min-heap. And initially push the next state of every element in the heap.
Note that you need to keep track of the indices of every element in the heap, present in the initial array.
Pick the top element, and change the state of that element in the state array.
Pop this element and push the next state in the heap.
At every operation, we are choosing the element whose next state is minimum hence there are only two possibilities:
1) Either the maximum element remains the same, and we return that element directly.
2) The next state of the popped element is the maximum.
We made sure changing the state of this element is the best option, as the next state of this element is the minimum.
Hence the maximum will be the least using this approach.

 ```
 
 import heapq

class Solution:

    def solve(self, A, B):

        pq = []
        n  = len(A)
        maxx = A[0]

        # Consider a min heap. And initially push the next state of every element in the heap.
        # Note that you need to keep track of the indices of every element in the heap, present in the initial array.
        for i in range(0, n):
            heapq.heappush(pq, [2*A[i], i])
            maxx = max(maxx, A[i])

        while(B > 0):

            # Pick the top element, and change the state of that element, in the state array.
            val, index = heapq.heappop(pq)
            maxx = max(maxx, val)
            new_val = val + A[index]

            # push the next state in the heap.
            heapq.heappush(pq, [new_val, index])
            B -= 1

        return maxx
 
 ```
