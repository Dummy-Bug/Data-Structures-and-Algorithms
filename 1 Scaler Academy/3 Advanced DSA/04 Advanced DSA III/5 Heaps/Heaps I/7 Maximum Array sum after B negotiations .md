### Problem Description

Given an array of integers A and an integer B. You must modify the array exactly B number of times. In a single modification, 
we can replace any one array element A[i] by -A[i].

You need to perform these modifications in such a way that after exactly B modifications, sum of the array must be maximum.



Problem Constraints
1 <= length of the array <= 5*105
1 <= B <= 5 * 106
-100 <= A[i] <= 100



Input Format
The first argument given is an integer array A.
The second argument given is an integer B.



Output Format
Return an integer denoting the maximum array sum after B modifications.



Example Input
Input 1:

 A = [24, -68, -29, -9, 84]
 B = 4
Input 2:

 A = [57, 3, -14, -87, 42, 38, 31, -7, -28, -61]
 B = 10


Example Output
Output 1:

 196
Output 2:

 362


Example Explanation
Explanation 1:

 Final array after B modifications = [24, 68, 29, -9, 84]
Explanation 2:

 Final array after B modifications = [57, -3, 14, 87, 42, 38, 31, 7, 28, 61]
 
 
 **Approach**
 This problem can simply be solved by just changing the minimum element A[i] to -A[i].

Keep on getting the minimum element from the array and multiply that element by -1. Do this exactly B times.

It is easy to observe that if the minimum element is zero, we can’t increase our answer by any modification.
If the minimum element is x < 0, then just change it to -x.
If the minimum element is x > 0 and the number of operations left is even. You do not need to change anything.
If the minimum element is x > 0 and the number of operations left is odd. We can directly change the number of operations left to 0 and set x to -x.

Now, just find the sum of all the elements.

 ```
 
import heapq;

class Solution:

    def solve(self, heap, B):

        heapq.heapify(heap);

        for i in range(B):

            heapq.heappush(heap,-1*heapq.heappop(heap));
        
        return sum(heap);
 
 ```
