### Problem Description

Given two binary strings A and B. Return their sum (also a binary string).

Problem Constraints
1 <= length of A <= 105

1 <= length of B <= 105

A and B are binary strings



Input Format
The two argument A and B are binary strings.



Output Format
Return a binary string denoting the sum of A and B



Example Input
Input 1:
A = "100"
B = "11"
Input 2:
A = "110"
B = "10"


Example Output
Output 1:
"111"
Output 2:
"1000"


Example Explanation
For Input 1:
The sum of 100 and 11 is 111.
For Input 2:
 
The sum of 110 and 10 is 1000.


**SOlution Approach**

Since the sizes of the two strings may be different, we first make the size of the smaller string equal to that of the bigger one by adding 
leading 0s for simplicity. Note that you can handle the addition without adding zeroes by adding a few if statements. After making sizes the same,
we add bits from the rightmost bit to the leftmost bit.
In every iteration, we must sum 3 bits: 2 bits of 2 given strings and carry.
The sum bit will be 1 if all 3 bits are set, or one of them is set.

So we can add all the bits and then take the remainder with 2 to get the current bit in the answer. How to find the carryover? 
Carry will be 1 if any of the two bits is set. So we can find carry by adding the bits and dividing the result by 2. Following is a 
step-by-step algorithm: 1. Make them equal-sized by adding 0s at the beginning of the smaller string. 2. Perform bit addition Boolean 
expression for adding 3 bits a, b, c Sum = (a + b + c) % 2 Carry = (a + b + c ) / 2;


```

class Solution:

	def addBinary(self, A, B):

        n1 = len(A); n2 = len(B);
        i  = n1 -1 ; j = n2 - 1;

        ans = '';carry = 0;

        while i >= 0 or j >= 0:

            a,b = 0,0;

            if i>=0:
                a = int(A[i]);
            if j>=0:
                b = int(B[j]);
            
            curr_sum = (a+b+carry)%2;
            carry    = (a+b+carry)//2;
            ans      = ans + str(curr_sum);

            i = i - 1; j = j - 1;
        
        if carry == 1:
            ans = ans + '1';
        
        return ans[::-1]

```
