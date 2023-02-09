### Problem Description

Given two integer arrays A and B of size N each which represent values and weights associated with N items respectively.

Also given an integer C which represents knapsack capacity.

Find out the maximum value subset of A such that sum of the weights of this subset is smaller than or equal to C.

NOTE:

You cannot break an item, either pick the complete item, or don’t pick it (0-1 property).


Problem Constraints
1 <= N <= 103

1 <= C <= 103

1 <= A[i], B[i] <= 103



Input Format
First argument is an integer array A of size N denoting the values on N items.

Second argument is an integer array B of size N denoting the weights on N items.

Third argument is an integer C denoting the knapsack capacity.



Output Format
Return a single integer denoting the maximum value subset of A such that sum of the weights of this subset is smaller than or equal to C.



Example Input
Input 1:

 A = [60, 100, 120]
 B = [10, 20, 30]
 C = 50
Input 2:

 A = [10, 20, 30, 40]
 B = [12, 13, 15, 19]
 C = 10


Example Output
Output 1:

 220
Output 2:

 0


Example Explanation
Explanation 1:

 Taking items with weight 20 and 30 will give us the maximum value i.e 100 + 120 = 220
Explanation 2:

 Knapsack capacity is 10 but each item has weight greater than 10 so no items can be considered in the knapsack therefore answer is 0.
 
 
 **Approach**
 
 There can be two cases for every item:

the item is included in the optimal subset.
not included in the optimal set.
Therefore, the maximum value that can be obtained from n items is max of following two values.

Maximum value obtained by n-1 items and W weight (excluding nth item).
Value of nth item plus maximum value obtained by n-1 items and W minus weight of the nth item (including nth item).
If weight of nth item is greater than W, then the nth item cannot be included and case 1 is the only possibility.

We will solve it by using DP with the bottom-up approach. Our knapsack size is W, we have to make maximum value to fill the knapsack.
A simple approach will be, how can we get maximum value if your knapsack size 1, then compute maximum value if knapsack size is 2 and so on….

Suppose dp[i][j] represents the maximum value that can be obtain considering first i items and a knapsack with a capacity of j.
Then our recurrence relation will look like:
dp[i][j]=max(dp[i-1][j] (When we don’t consider this item) or dp[i-1][j-wt[i]]+val[i] (When we consider this item) )

Time Complexity: O(NW)

 ```
 
 import sys;
sys.setrecursionlimit(10**9);

class Solution:

    def solve(self, A, B, C):

        self.dp = [[-1 for j in range(C+1)] for i in range(len(A)+1)];

        return self.funcn(C,B,A,len(A));
        

    def funcn(self,capacity,wt_array,val_array,n):
        
        if n <= 0:
            return 0
            
        if self.dp[n][capacity] != -1:
            return self.dp[n][capacity]
            
        if wt_array[n-1] <= capacity: # if value's weight is lesser then we have two choices.
        
            value_considered = val_array[n-1] + self.funcn(capacity - wt_array[n-1],wt_array,val_array,n-1)
                            #  calling the function with new capacity and new size of the array
        
            not_considered   = 0 + self.funcn(capacity,wt_array,val_array,n-1)
                            # if not considered then just decrease the size of the array.  
                            
            self.dp[n][capacity] = max(value_considered,not_considered)
            return self.dp[n][capacity]
            
        else:
            
            return self.funcn(capacity,wt_array,val_array,n-1)


 
 ```
