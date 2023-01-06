### Problem Description

Given an array A having N positive numbers. You have to find the number of Prime subsequences of A.

A Prime subsequence is one that has only prime numbers, for example [2, 3], [5] are the Prime subsequences where [2, 4] and [1, 2, 3, 4] are not.



Input Format

The first argument given is an Array A, having N integers.
Output Format

Return an integer X, i.e number of Prime subsequences. 
As X can be very large print X % (1000000007), here % is modulus operator.
Constraints

1 <= N <= 1e3
1 <= A[i] <= 1e6
For Example

Input:
    A = [1, 2, 3]
Output:
     3

Explanation:
    no. Subsequences      Prime subsequences
    1.  [1]                     No
    2.  [1, 2]                  No
    3.  [1, 3]                  No
    4.  [1, 2, 3]               No
    5.  [2]                     Yes
    6.  [2, 3]                  Yes
    7.  [3]                     Yes
    8.  []                      No

    here we have 3 subsequences(5, 6, 7) those have only prime number(s).
    
**Solution Approach**

Let M be the number of prime integers in an array, then the number of Prime Subsequences will be ((2 ^ M) - 1).
Can you prove this?

```

class Solution:
    
    def solve(self, A):

        prime_count = 0;
        mod = 1000000007;
        for i in range(len(A)):
            if  (A[i] > 1) & (self.prime(A[i])):
                prime_count = (prime_count + 1);
        
        return (2**prime_count)%mod-1;
    
    def prime(self,n):

        for i in range(2,int(n**0.5) + 1):
            if (n%i) == 0:
                return 0;
        
        return 1

```
