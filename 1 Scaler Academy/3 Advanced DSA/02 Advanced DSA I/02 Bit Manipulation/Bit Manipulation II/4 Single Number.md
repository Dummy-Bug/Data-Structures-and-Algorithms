### Problem Description

Given an array of positive integers A, two integers appear only once, and all the other integers appear twice.
Find the two integers that appear only once.

Note: Return the two numbers in ascending order.


Problem Constraints
2 <= |A| <= 100000
1 <= A[i] <= 109



Input Format
The first argument is an array of integers of size N.



Output Format
Return an array of two integers that appear only once.



Example Input
Input 1:
A = [1, 2, 3, 1, 2, 4]
Input 2:

A = [1, 2]


Example Output
Output 1:
[3, 4]
Output 2:

[1, 2]


Example Explanation
Explanation 1:
3 and 4 appear only once.
Explanation 2:

1 and 2 appear only once.

**Solution Approach**

If we use additional memory, we can directly store the count and find the integers which occur only once.
To solve without additional memory, We can use the xor operation, as the Xor of two integers gives 0.
Take the Xor of all the integers of the array. Integers that occur twice will not contribute anything to the xor value.
Suppose that the ith bit is set in the xor value, which means that exactly one of the two required numbers has that bit set.
If we then divide the array integers into two groups: one group contains all integers with the ith bit set, and the other group 
contains integers with 0 at the ith bit.
Each group includes one of the two required numbers, and for the rest of the numbers, both of their occurrences will be in the same group.
Now, Xor of integers in the first group gives a number that occurs exactly once. Xor of integers in the second group provides another number 
that appears exactly once.

```

class Solution:

    def solve(self, A):

        xor = 0; n = len(A);

        for num in A:
            xor = xor^num;
        
        bit_pos = -1;
        for i in range(32):
            if (xor>>i)&1 == 1:
                bit_pos = i;
                break;
        
        set_bit = unset_bit = 0;

        for num in A:
            if (num>>bit_pos)&1 == 1:
                set_bit = set_bit^num;
            
            else:
                unset_bit = unset_bit^num;
        
        return sorted([set_bit,unset_bit]);

```
