### Problem Description

You are given an even number N and you need to represent the given number as the sum of primes. The prime numbers do not necessarily have to be 
distinct. It is guaranteed that at least one possible solution exists.

You need to determine the minimum number of prime numbers needed to represent the given number.

Input

The first argument contains an integer N,the number you need to represent (2<=N<=10^9).
Output

Return an integer which is the minimum number of prime numbers needed to represent the given number N.
Examples

Input

26
Output

2
Explanation

Testcase 1-

You can represent 26 as: 13+13
So we require minimum of 2 prime numbers to represent the number 26.

**Approach**

Goldbach's conjecture states that every even integer greater than 2 can be expressed as the sum of two primes.

Bonus : This conjecture is not proven yet but verified uptil 4*10^18 integers.

And 2 is already a prime number.

```

class Solution:

    def solve(self, A):
        if A == 2:
            return 1;a
        return 2

```
