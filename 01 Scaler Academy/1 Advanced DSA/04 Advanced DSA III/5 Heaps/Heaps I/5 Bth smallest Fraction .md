### Problem Description

Given a sorted array of integers A which contains 1 and some number of primes.
Then, for every p < q in the list, we consider the fraction p / q.

What is the B-th smallest fraction considered?

Return your answer as an array of integers, where answer[0] = p and answer[1] = q.



Problem Constraints
1 <= length(A) <= 2000
1 <= A[i] <= 30000
1 <= B <= length(A)*(length(A) - 1)/2



Input Format
The first argument of input contains the integer array, A.
The second argument of input contains an integer B.



Output Format
Return an array of two integers, where answer[0] = p and answer[1] = q.



Example Input
Input 1:

 A = [1, 2, 3, 5]
 B = 3
Input 2:

 A = [1, 7]
 B = 1


Example Output
Output 1:

 [2, 5]
Output 2:

 [1, 7]


Example Explanation
Explanation 1:

 The fractions to be considered in sorted order are:
 [1/5, 1/3, 2/5, 1/2, 3/5, 2/3]
 The third fraction is 2/5.
Explanation 2:

 The fractions to be considered in sorted order are:
 [1/7]
 The first fraction is 1/7.

**Approach**
The brute-force solution for this problem would be to generate all the possible combinations, sort them by their value and then return the
Kth element.

The complexity of this solution would be O(N2log2(N2),
which exceeds the allocated time limit.

Instead, what we can do is use a min-heap such that its size never exceeds N.
We can achieve this by maintaining a heap that stores the following structure:

(A[j]/A[i], i, j)
We know that if we increase the denominator, the value of the fraction decreases.

Initially, we push all the elements divided by the largest element, as they will be the smallest fractions.
Now, we remove the smallest element in the min-heap,
increase its denominator if possible and then insert it back into the min-heap.

After doing this B times, the element on the top will be the B-th smallest fraction.
The complexity of this solution will be O(N2log2(N)).

```

import heapq;

class Solution:

    def solve(self, A, B):

        heap = [];
        heapq.heapify(heap);

        for i in range(len(A)):
            for j in range(i+1,len(A)):
                
                fraction = (A[i]/A[j])*1.0
                heapq.heappush(heap,[fraction,A[i],A[j]]);
        
        for _ in range(B):
            fraction,p,q = heapq.heappop(heap);
        return [p,q];

```
