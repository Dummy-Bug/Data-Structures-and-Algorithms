### Problem Description

Given two integers A and B. Find the value of A-1 mod B where B is a prime number and gcd(A, B) = 1.
A-1 mod B is also known as modular multiplicative inverse of A under modulo B.

Problem Constraints
1 <= A <= 109
1<= B <= 109
B is a prime number



Input Format
First argument is an integer A.
Second argument is an integer B.



Output Format
Return an integer denoting the modulor inverse



Example Input
Input 1:

 A = 3
 B = 5
Input 2:

 A = 6
 B = 23


Example Output
Output 1:

 2
Output 2:

 4


Example Explanation
Explanation 1:

 Let's say A-1 mod B = X, then (A * X) % B = 1.
 3 * 2 = 6, 6 % 5 = 1.
Explanation 2:

 Similarly, (6 * 4) % 23 = 1.


**Solution Approach**

Fermats’s little theorem:

AB-1 ≡ 1 (mod B) where B is prime and A is not a multiple of B.
Multiply by A-1 on both sides, We get

AB-2 ≡ A-1 (mod B) where B is prime and A is not a multiple of B.
We just have to calculate AB-2 (mod B). This will be the modular multiplicative inverse of A under modulo B.


```

class Solution:
    import math;

    def solve(self, A, B):

        return (self.helper(A,B-2,B))%B;
    
    def helper(self,A,B,mod):

        if B == 0:
            return 1;
        
        temp = self.helper(A,B>>1,mod);
        temp = (temp*temp)%mod;
        
        if (B&1) == 0:
            return temp;
        else:
            return (temp*A)%mod;

```
