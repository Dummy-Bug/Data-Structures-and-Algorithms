### Problem Description

The gray code is a binary numeral system where two successive values differ in only one bit.

Given a non-negative integer A representing the total number of bits in the code, print the sequence of gray code.

A gray code sequence must begin with 0.



Problem Constraints
1 <= A <= 16



Input Format
The first argument is an integer A.



Output Format
Return an array of integers representing the gray code sequence.



Example Input
Input 1:

A = 2
Input 1:

A = 1


Example Output
output 1:

[0, 1, 3, 2]
output 2:

[0, 1]


Example Explanation
Explanation 1:

for A = 2 the gray code sequence is:
    00 - 0
    01 - 1
    11 - 3
    10 - 2
So, return [0,1,3,2].
Explanation 1:

for A = 1 the gray code sequence is:
    00 - 0
    01 - 1
So, return [0, 1].


**Approach**

Note the following :

Let G(n) represent a gray code of n bits.
Let R(n) denote the reverse of G(n).

Note that we can construct.
G(n+1) as the following :
0G(n)
1R(n)

Where 0G(n) means all elements of G(n) prefixed with 0 bit and 1R(n) means all elements of R(n) prefixed with 1.
Note that the last element of G(n) and the first element of R(n) are the same. So the above sequence is valid.

Example G(2) to G(3) :
0 00
0 01
0 11
0 10
1 10
1 11
1 01
1 00

```

import sys
sys.setrecursionlimit(10**6)
class Solution:

    def grayCode(self, A):
        def graycode(n,ans):
            if n == 0:
                return
            if n == 1:
                ans.append(0)
                ans.append(1)
            graycode(n-1,ans)

            msb = 1<< n-1
            if n > 1:
                s = len(ans) - 1
                while s >= 0:
                    ans.append(ans[s]+msb)
                    s -= 1
            return ans


        return graycode(A,[])

```

```

class Solution:

    def grayCode(self, A):
        ans = []
        # G[n] = n ^ (n >> 1)
        for i in range(2 ** A):
            ans.append(i ^ (i >> 1))
        return ans

```
