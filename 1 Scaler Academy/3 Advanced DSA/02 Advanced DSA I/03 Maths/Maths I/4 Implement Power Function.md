### Problem Description

Implement pow(A, B) % C.
In other words, given A, B and C, Find (AB % C).

Note: The remainders on division cannot be negative. In other words, make sure the answer you return is non-negative.



Problem Constraints
-109 <= A <= 109
0 <= B <= 109
1 <= C <= 109


Input Format
Given three integers A, B, C.


Output Format
Return an integer.


Example Input
A = 2, B = 3, C = 3


Example Output
2


Example Explanation
23 % 3 = 8 % 3 = 2

**Solution Approach**

There are two important things to note here:

1) Overflow situation: Note that if x is large enough, multiplying x to the answer might overflow in integer.

2) Multiplying x one by one to the answer is O(n). We are looking for something better than O(n).

If n is even, note the following:

x ^ n = (x * x) ^ n/2

Can you use the above observation to develop a solution better than O(n)?

```

class Solution:

    def pow(self, A, B, C):

        return self.helper(A,B,C)
    
    def helper(self,A,B,mod):

        if A == 0 or B == 1:
            return A%mod;
        if B == 0:
            return 1;
        
        if B%2 == 0:
            temp = self.helper(A,B//2,mod)
            return (temp*temp)%mod;
        else:
            temp = self.helper(A,B//2,mod)
            return (temp*temp*A)%mod;

```
