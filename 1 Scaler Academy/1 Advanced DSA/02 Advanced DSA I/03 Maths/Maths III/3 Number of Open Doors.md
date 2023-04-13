### Problem Description

Given an integer A, which denotes the number of doors in a row numbered 1 to A. All the doors are closed initially.

A person moves to and fro, changing the states of the doors as follows: the person opens a door that is already closed and closes a door that 
is already opened.

In the first go, he/she alters the states of doors numbered 1, 2, 3, … , A.
In the second go, he/she alters the states of doors numbered 2, 4, 6 ….
In the third go, he/she alters the states of doors numbered 3, 6, 9 …
This continues till the A'th go in, which you alter the state of the door numbered A.

Find and return the number of open doors at the end of the procedure.



Problem Constraints
1 <= A <= 109



Input Format
The only argument given is integer A.



Output Format
Return the number of open doors at the end of the procedure.



Example Input
Input 1:

 A = 5
Input 2:

 A = 6


Example Output
Output 1:

 2
Output 2:

 2 


Example Explanation
Input 1:

 In the first go, he/she alters the states of doors numbered 1, 2, 3, 4, 5. Now, all doors are open.
 In the second go, he/she closes the doors numbered 2, 4.
 In the third go, he/she closes the door numbered 3.
 In the fourth go, he/she open the door numbered 4.
 In the fifth go, he/she closes the door numbered 5.
 Doors opened at the end are 1 and 4.
Input 2:

 In the first go, he/she alters the states of doors numbered 1, 2, 3, 4, 5, 6. Now, all doors are open.
 In the second go, he/she closes the doors numbered 2, 4, 6.
 In the third go, he/she closes the door numbered 3 and opens door 6.
 In the fourth go, he/she open the door numbered 4.
 In the fifth go, he/she closes the door numbered 5.
 In the sixth go, he/she closes the door numbered 6.
 Doors opened at the end are 1 and 4.
 
 
 **Solution Approach**
 
 We observe that the number of time a door X alter its state is the number of factors of that door X.
If the number of factors is even, then the door will be closed; else, it will be open.

So, we need to find the numbers between 1 to A for which the number of factors is odd.

This leads to a very interesting observation that only the number which is perfect square has an odd number of factors.
How?
If ‘a’ is a factor of ‘X’, then there will be a ‘b’ such that ‘a’ * ‘b’ = X.
Only a number that is perfectly square has a factor ‘a’ such that ‘a’ * ‘a’ = X.

So we will count the number of perfect squares between 1 and A, and that will be sqrt(A).


```

class Solution:
    import math;
    
    def solve(self, A):
        
        return int(math.pow(A,0.5));

```
