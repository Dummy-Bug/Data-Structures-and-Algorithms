### Problem Description 

Problem Description
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

```

def knapSack(W, wt, val, n):
    dp = [[0 for x in range(W + 1)] for x in range(n + 1)]
    # Build table dp[][] in bottom up manner
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                dp[i][w] = 0
            elif wt[i - 1] <= w:
                dp[i][w] = max(val[i - 1] + dp[i - 1][w - wt[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][W]


class Solution:

    def solve(self, A, B, C):
        return knapSack(C, B, A, len(A))


```
