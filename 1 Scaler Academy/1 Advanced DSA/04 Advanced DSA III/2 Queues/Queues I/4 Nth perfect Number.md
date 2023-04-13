### Problem Description

Given an integer A, you have to find the Ath Perfect Number.

A Perfect Number has the following properties:

It comprises only 1 and 2.

The number of digits in a Perfect number is even.

It is a palindrome number.

For example, 11, 22, 112211 are Perfect numbers, where 123, 121, 782, 1 are not.



Problem Constraints
1 <= A <= 100000



Input Format
The only argument given is an integer A.



Output Format
Return a string that denotes the Ath Perfect Number.



Example Input
Input 1:

 A = 2
Input 2:

 A = 3


Example Output
Output 1:

 22
Output 2:

 1111


Example Explanation
Explanation 1:

First four perfect numbers are:
1. 11
2. 22
3. 1111
4. 1221
Explanation 2:

First four perfect numbers are:
1. 11
2. 22
3. 1111
4. 1221


**Approach**

Can you precompute the answer of all times and
then answer as the queries come in??
It appears that we can use Queue and precompute for 100000 Perfect numbers.
First insert “1” and “2” and then use s -> s+’1’
and s -> s+’2’
to fill up the queue.

```

from collections import deque;

class Solution:

    def solve(self, A):

        q = deque();

        q.append('11');
        q.append('22');
        count = 2; num_delete = 0;

        while count < A:
            string = q.popleft();
            num_delete += 1;

            size = len(string);
            q.append(string[0:size//2]+'11'+string[size//2:]);
            q.append(string[0:size//2]+'22'+string[size//2:]);

            count += 2;
        
        while num_delete < A-1:
            string = q.popleft();
            num_delete += 1;
        
        return int(q.popleft());

```
