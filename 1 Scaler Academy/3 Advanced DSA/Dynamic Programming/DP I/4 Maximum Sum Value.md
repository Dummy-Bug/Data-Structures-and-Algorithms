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
