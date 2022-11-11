### Problem Description

You are given an array A of N integers and three integers B, C, and D.

You have to find the maximum value of A[i]*B + A[j]*C + A[k]*D, where 1 <= i <= j <= k <= N.

https://www.geeksforgeeks.org/given-array-three-numbers-maximize-x-ai-y-aj-z-ak/


```

class Solution:

    def solve(self, A, B, C, D):
        # The first key observation is i ≤ j ≤ k, so x*a[i] will always be the 
        # left maximum, and z*a[k] will always be the right maximum

        left_max  = [A[0]*B];
        right_max = [A[-1]*D]*len(A);

        for i in range(1,len(A)):
            num = A[i];
            left_max.append(max(num*B,left_max[-1]));
        # print(right_max)
        for i in range(len(A)-2,-1,-1):
            right_max[i] = max(A[i]*D,right_max[i+1])
        # print(left_max,right_max);
        result =  float('-inf');
        for i in range(len(A)):
            result = max(result,left_max[i]+A[i]*C+right_max[i]);
        return result;


```

**Using DP**

Create a dynamic programming table of size n * 3. In this, dp[i][0] stores maximum of value B * A[p] for p between 1 and i. Similarly dp[i][1] stores the maximum value of B * A[p] + C * A[q] such that p <= q <= i and dp[i][2] stores maximum value of B * A[p] + C * A[q] + D * A[r] for p <= q <= r <= i.

To calculate the dp:

dp[i][0] = max(dp[i-1][0], B * A[i])

dp[i][1] = max(dp[i-1][1], dp[i][0] + C * A[i])

dp[i][2] = max(dp[i-1][2], dp[i][1] + D * A[i])

The answer will be stored in dp[n][2]


```


class Solution:

    def solve(self, A, B, C, D):
        n = len(A)
        # dp array to store answer of previous states
        dp = [[-5e9 for i in range(3)] for j in range(n+1)]

        # Initialize the dp array with minus infinity

        for i in range(1, n+1):
            # Maximum value of A[i] * B
            dp[i][0] = max(dp[i-1][0], A[i-1] * B)
            # Maximum value of A[i] * B + A[j] * C
            dp[i][1] = max(dp[i-1][1], dp[i][0] + A[i-1] * C)
            # Maximum value of A[i] * B + A[j] * C + A[k] * D
            dp[i][2] = max(dp[i-1][2], dp[i][1] + A[i-1] * D);
        
        return dp[n][2]        # return the answer.

```
