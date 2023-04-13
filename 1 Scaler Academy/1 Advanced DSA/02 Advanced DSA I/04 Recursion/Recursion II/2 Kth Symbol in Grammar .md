### Problem Description

On the first row, we write a 0. Now in every subsequent row, we look at the previous row and replace each occurrence of 0 with 01, 
and each occurrence of 1 with 10.

Given row number A and index B, return the Bth indexed symbol in row A. (The values of B are 1-indexed.).



Problem Constraints
1 <= A <= 20

1 <= B <= 2A - 1



Input Format
First argument is an integer A.

Second argument is an integer B.



Output Format
Return an integer denoting the Bth indexed symbol in row A.



Example Input
Input 1:

 A = 2
 B = 1
Input 2:

 A = 2
 B = 2


Example Output
Output 1:

 0
Output 2:

 1


Example Explanation
Explanation 1:

 Row 1: 0
 Row 2: 01
Explanation 2:

 Row 1: 0
 Row 2: 01
 
 
 **Approach**
 
 When
A = 1 -> 0
A = 2 ->01
A = 3 ->0110

As we can see that there are two part in string (when A>=2)
first part is repeating of (A-1)th> step and second part is also compliment of (A-1)th step

for A = 3 -> first part - 01 ( it is same as when A == 2) second part- 10 ( compliment of when A == 2)

We know that on every expansion, the length of String is 2(A-1)

so what we can do when B value is <= mid we can search the result in first part of (A-1)th step solve(A-1, B)

and when B > mid we can search the result in (A-1)th step but compliment of that index to get the actual index in 1st part we have to do B - mid.
 
 
 
 ```
 
 class Solution:

    def solve(self, A, B):

        if A == 1 or B == 1:
            return 0;
        
        symbol = self.solve(A-1,(B+1)//2);

        if B&1 != 1:
            return (symbol^1); # Toggling using xor;
        
        else:
            return symbol;
 
 ```
