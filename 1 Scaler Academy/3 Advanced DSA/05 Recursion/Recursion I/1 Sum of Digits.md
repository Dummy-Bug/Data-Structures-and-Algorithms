### Problem Description

Given a number A, we need to find the sum of its digits using recursion.



Problem Constraints
1 <= A <= 109



Input Format
The first and only argument is an integer A.



Output Format
Return an integer denoting the sum of digits of the number A.



Example Input
Input 1:

 A = 46
Input 2:

 A = 11


Example Output
Output 1:

 10
Output 2:

 2


Example Explanation
Explanation 1:

 Sum of digits of 46 = 4 + 6 = 10
Explanation 2:

 Sum of digits of 11 = 1 + 1 = 2


**Approach**

Step by step process for better understanding of how the algorithm works.
Let the number be 12345.
Step 1-> 12345 % 10 which is equal-too 5 + ( send 12345/10 to next step ),
Step 2-> 1234 % 10 which is equal-too 4 + ( send 1234/10 to next step ),
Step 3-> 123 % 10 which is equal-too 3 + ( send 123/10 to next step ),
Step 4-> 12 % 10 which is equal-too 2 + ( send 12/10 to next step ),
Step 5-> 1 % 10 which is equal-too 1 + ( send 1/10 to next step ),
Step 6-> 0 algorithm stops.



```

class Solution:

    def solve(self, A):

        if A < 10:
            return A;
        
        return self.solve(A//10) + A%10;


```
