### Problem Description

Divide two integers without using multiplication, division and mod operator.

Return the floor of the result of the division.

Also, consider if there can be overflow cases i.e output is greater than INT_MAX, return INT_MAX.

NOTE: INT_MAX = 2^31 - 1



Problem Constraints
-231 <= A, B <= 231-1

B != 0



Input Format
The first argument is an integer A denoting the dividend.
The second argument is an integer B denoting the divisor.



Output Format
Return an integer denoting the floor value of the division.



Example Input
Input 1:

 A = 5
 B = 2
Input 2:

 A = 7
 B = 1


Example Output
Output 1:

 2
Output 2:

 7


Example Explanation
Explanation 1:

 floor(5/2) = 2


**Solution Approach**

Think in terms of bits.

How do you divide with bits?

How do you determine the most significant bit in the answer?
Iterate on the bit position ‘i’ from 31 to 1 and find the first bit for which divisor«i is less than the dividend.

How do you use (1) to move forward similarly?

```

class Solution:

    def divide(self, A, B):

        if A == 0:
            return 0
        INT_MAX = (1<<31)-1 ; INT_MIN = -(1<<31)
        n = A ;m = B
        
        sign = 1
        if (A < 0 and B > 0) or (A > 0 and B < 0):
            sign = -1
        # int range is [-2^31 to 2^31-1], so if we take mod then we cannot
        n = abs(n) ; m = abs(m) # store |-2^31| Hence data type would be lonh long int 
        
        q = 0 ; t = 0
        
        for i in range(31, -1, -1):
            if (m << i) <= n:
                n = n - (m << i); # Bewware of Operator Presednece;
                q = q + (1 << i);
        if sign < 0: 
            q = -q
        
        if q >= INT_MAX :
            return INT_MAX
        return q
        
```
