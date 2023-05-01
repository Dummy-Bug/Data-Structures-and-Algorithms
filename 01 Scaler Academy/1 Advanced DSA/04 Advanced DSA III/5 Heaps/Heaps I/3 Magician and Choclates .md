### Problem Description

Given N bags, each bag contains Bi chocolates. There is a kid and a magician.
In a unit of time, the kid can choose any bag i, and eat Bi chocolates from it, then the magician will fill the ith bag with floor(Bi/2) 
chocolates.

Find the maximum number of chocolates that the kid can eat in A units of time.

NOTE:

floor() function returns the largest integer less than or equal to a given number.
Return your answer modulo 109+7


Problem Constraints
1 <= N <= 100000
0 <= B[i] <= INT_MAX
0 <= A <= 105



Input Format
The first argument is an integer A.
The second argument is an integer array B of size N.



Output Format
Return an integer denoting the maximum number of chocolates the kid can eat in A units of time.



Example Input
Input 1:

 A = 3
 B = [6, 5]
Input 2:

 A = 5
 b = [2, 4, 6, 8, 10]


Example Output
Output 1:

 14
Output 2:

 33


Example Explanation
Explanation 1:

 At t = 1 kid eats 6 chocolates from bag 0, and the bag gets filled by 3 chocolates. 
 At t = 2 kid eats 5 chocolates from bag 1, and the bag gets filled by 2 chocolates. 
 At t = 3 kid eats 3 chocolates from bag 0, and the bag gets filled by 1 chocolate. 
 so, total number of chocolates eaten are 6 + 5 + 3 = 14
Explanation 2:

 Maximum number of chocolates that can be eaten is 33.
 
 **Approach**
 
 The solution to this problem can be found greedily.

At any time t, the kid will always choose the bag with the maximum number of chocolates and consume all its chocolates.
So we need to maintain the current maximum size among all bags for every time t = 1, … , B and also update the sizes of the bags.

This can be done using a max heap : https://en.wikipedia.org/wiki/Min-max_heap

Time Complexity:- O(AlogN + N)
Space Complexity:- O(N)

 ```
 
 import heapq;

class Solution:
	def nchoc(self, A, B):
        
        heap = []; mod = 1000000000+7;

        for bag in B:
            heap.append(-1*bag);

        heapq.heapify(heap);
        total_choclates = 0;

        for _ in range(A):

            curr_choclates = -1*heapq.heappop(heap);
            total_choclates = (total_choclates+ curr_choclates)%mod;

            heapq.heappush(heap,-1*(curr_choclates//2));
        
        return total_choclates;

 ```
