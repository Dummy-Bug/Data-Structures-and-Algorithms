### Problem Description

Given a knapsack weight A and a set of items with certain value B[i] and weight C[i], we need to calculate maximum amount that could fit
in this quantity.

This is different from classical Knapsack problem, here we are allowed to use unlimited number of instances of an item.



Problem Constraints
1 <= A <= 1000

1 <= |B| <= 1000

1 <= B[i] <= 1000

1 <= C[i] <= 1000



Input Format
First argument is the Weight of knapsack A

Second argument is the vector of values B

Third argument is the vector of weights C



Output Format
Return the maximum value that fills the knapsack completely



Example Input
Input 1:

A = 10
B = [5]
C = [10]
Input 2:

A = 10
B = [6, 7]
C = [5, 5]


Example Output
Output 1:

 5
Output 2:

14


Example Explanation
Explanation 1:

Only valid possibility is to take the given item.
Explanation 2:

Take the second item twice.


```

import sys;
sys.setrecursionlimit(10**9);

class Solution:

    def solve(self, A, B, C):
        n = len(B)
        self.dp = [[ -1 for i in range( 0,A+1)]for j in range( 0,n+1 )] # +1 so that we can have value of dp[val][w]
        # 2D array because two variables are changing in our recursive function.
        # only take the variables that are changing ignore the rest of the variables for dp array.
        
        return self.funcn(A,C,B,n);

    def funcn(self,capacity,wt_array,val_array,n):
        
        if n <= 0:
            return 0
            
        if self.dp[n][capacity] != -1:
            return self.dp[n][capacity]
            
        if wt_array[n-1] <= capacity: # if value's weight is lesser then we have two choices.
        
            value_considered = val_array[n-1] + self.funcn(capacity - wt_array[n-1],wt_array,val_array,n)
                            #  calling the function with new capacity and new size of the array
        
            not_considered   = 0 + self.funcn(capacity,wt_array,val_array,n-1)
                            # if not considered then just decrease the size of the array.  
                            
            self.dp[n][capacity] = max(value_considered,not_considered)
            return self.dp[n][capacity]
            
        else:
            
            return self.funcn(capacity,wt_array,val_array,n-1)


```


```

public class Solution {
    public int solve(int A, int[] B, int[] C) {
        int W = A;
        int[] dp = new int[W + 1];
        Arrays.fill(dp, 0);
        for (int i = 0; i <= W; i++)
            for (int j = 0; j < B.length; j++)
                if (C[j] <= i)
                    dp[i] = Math.max(dp[i], dp[i - C[j]] + B[j]);
        return dp[W];
    }
}

```
