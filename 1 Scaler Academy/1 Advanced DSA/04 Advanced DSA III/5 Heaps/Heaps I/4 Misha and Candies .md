### Problem Description

Misha loves eating candies. She has been given N boxes of Candies.

She decides that every time she will choose a box having the minimum number of candies, eat half of the candies and put the remaining candies in the other box that has the minimum number of candies.
Misha does not like a box if it has the number of candies greater than B so she won't eat from that box. Can you find how many candies she will eat?

NOTE 1: If a box has an odd number of candies then Misha will eat the floor(odd / 2).

NOTE 2: The same box will not be chosen again.



Problem Constraints
1 <= N <= 105

1 <= A[i] <= 105

1 <= B <= 106



Input Format
The first argument is A an Array of Integers, where A[i] is the number of candies in the ith box.
The second argument is B, the maximum number of candies Misha like in a box.



Output Format
Return an integer denoting the number of candies Misha will eat.



Example Input
Input 1:

 A = [3, 2, 3]
 B = 4
Input 2:

 A = [1, 2, 1]
 B = 2


Example Output
Output 1:

 2
Output 2:

 1


Example Explanation
Explanation 1:

 1st time Misha will eat from 2nd box, i.e 1 candy she'll eat and will put the remaining 1 candy in the 1st box.
 2nd time she will eat from the 3rd box, i.e 1 candy she'll eat and will put the remaining 2 candies in the 1st box.
 She will not eat from the 3rd box as now it has candies greater than B.
 So the number of candies Misha eat is 2.
Explanation 2:

 1st time Misha will eat from 1st box, i.e she can't eat any and will put the remaining 1 candy in the 3rd box.
 2nd time she will eat from the 3rd box, i.e 1 candy she'll eat and will put the remaining 1 candies in the 2nd box.
 She will not eat from the 2nd box as now it has candies greater than B.
 So the number of candies Misha eat is 1.
 
 **Approach**
 
 The main task is to optimally get the box with the least number of candies each time.
Think how you can get a box having the minimum number of candies in O(log(n))?

You can use a priority queue or min-heap to get a box having the minimum number of candies in O(log(n)).

 ```
 
 import heapq;

class Solution:

    def solve(self, heap, B):

        heapq.heapify(heap);
        num_candies = 0;

        while len(heap)>1:

            curr_candies = heapq.heappop(heap);
            if curr_candies>B:
                return num_candies;
            
            num_candies += curr_candies//2;

            heapq.heappush(heap,heapq.heappop(heap)+curr_candies - curr_candies//2);
        
        curr_candies = heapq.heappop(heap);

        if curr_candies <= B:
            num_candies += curr_candies//2;
        return num_candies;


 ```
