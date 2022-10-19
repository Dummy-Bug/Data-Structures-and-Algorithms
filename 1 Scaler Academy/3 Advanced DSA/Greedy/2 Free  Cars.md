

Problem Description
Given two arrays, A and B of size N. A[i] represents the time by which you can buy the ith car without paying any money.

B[i] represents the profit you can earn by buying the ith car. It takes 1 minute to buy a car, so you can only buy the ith car when the current time <= A[i] - 1.

Your task is to find the maximum profit one can earn by buying cars considering that you can only buy one car at a time.

NOTE:

You can start buying from time = 0.
Return your answer modulo 109 + 7.


Problem Constraints
1 <= N <= 105
1 <= A[i] <= 109
0 <= B[i] <= 109



Input Format
The first argument is an integer array A represents the deadline for buying the cars.
The second argument is an integer array B represents the profit obtained after buying the cars.



Output Format
Return an integer denoting the maximum profit you can earn.



Example Input
Input 1:

 A = [1, 3, 2, 3, 3]
 B = [5, 6, 1, 3, 9]
Input 2:

 A = [3, 8, 7, 5]
 B = [3, 1, 7, 19]


Example Output
Output 1:

 20
Output 2:

 30


Example Explanation
Explanation 1:

 At time 0, buy car with profit 5.
 At time 1, buy car with profit 6.
 At time 2, buy car with profit 9.
 At time = 3 or after , you can't buy any car, as there is no car with deadline >= 4.
 So, total profit that one can earn is 20.
Explanation 2:

 At time 0, buy car with profit 3.
 At time 1, buy car with profit 1.
 At time 2, buy car with profit 7.
 At time 3, buy car with profit 19.
 We are able to buy all cars within their deadline. So, total profit that one can earn is 30.
 

**Notes**

-> Using Maps but the Time Complexity is Quadratic 

```

import sys;
sys.setrecursionlimit(10**9);
class Solution:

    def solve(self, A, B):

        self.mod = 1000000000+7;

        temp_arr = []; deadlines_map = dict(); self.result = 0;

        for i in range(len(A)):
            temp_arr.append([ B[i],A[i] ]);
            deadlines_map[A[i]] = False;
     
        temp_arr.sort();
        for i  in range(len(temp_arr)-1,-1,-1):

            curr_profit , curr_deadline = temp_arr[i][0], temp_arr[i][1];
            self.check(curr_profit,curr_deadline,deadlines_map);

        return self.result;
    
    def check(self,profit,deadline,deadlines_map):
            
        if deadline < 1 :
            return 
        elif deadline in deadlines_map and deadlines_map[deadline] == False:
            self.result = (self.result+profit)%self.mod; 
            deadlines_map[deadline] = True;
            return;
        elif deadline not in deadlines_map:
            deadlines_map[deadline] = True;
            self.result = (self.result+profit)%self.mod;
            return 
        else:
            self.check(profit,deadline-1,deadlines_map);

```


**Approach 2**

-> Using MinHeap

*If at any time we have the option to buy a car which gives more profit than any of the car already taken.

At a particular time, We can buy a car or not.

If we are able to buy all the cars, then it’s fine. If not then we should remove a car with minimum profit which we had bought earlier and take the car with more profit.

Think why this will give us maximum profit.*


```

import heapq;

class Solution:

    def solve(self, A, B):

        temp_arr = [];
        for i in range(len(A)):
            temp_arr.append([A[i],B[i]]);
        
        temp_arr.sort();

        curr_time = 1; minheap = [];
        heapq.heapify(minheap);

        for i in range(len(temp_arr)):
            curr_deadline = temp_arr[i][0];
            curr_profit   = temp_arr[i][1];

            if curr_deadline>=curr_time:
                heapq.heappush(minheap,curr_profit);
                curr_time += 1;
                continue;

            min_profit = heapq.heappop(minheap);

            better_profit = max(min_profit,curr_profit);
            heapq.heappush(minheap,better_profit);
        
        total_profit = 0; mod = 1000000000+7;
        while len(minheap)>0:
            total_profit = ( total_profit+heapq.heappop(minheap) )%mod;
        
        return total_profit;


```
