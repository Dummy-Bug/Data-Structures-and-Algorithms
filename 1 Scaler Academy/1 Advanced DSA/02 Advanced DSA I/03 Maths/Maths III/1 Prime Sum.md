### Problem Description

Given an even number A ( greater than 2 ), return two prime numbers whose sum will be equal to the given number.

If there is more than one solution possible, return the lexicographically smaller solution.

If [a, b] is one solution with a <= b, and [c,d] is another solution with c <= d, then 
[a, b] < [c, d], If a < c OR a==c AND b < d. 
NOTE: A solution will always exist. Read Goldbach's conjecture.



Problem Constraints
4 <= A <= 2*107



Input Format
First and only argument of input is an even number A.



Output Format
Return a integer array of size 2 containing primes whose sum will be equal to given number.



Example Input
 4


Example Output
 [2, 2]


Example Explanation
There is only 1 solution for A = 4.

```

class Solution:
    def primesum(self, n):
        
        for i in range(2, n):
            if self.is_prime(i) and self.is_prime(n - i):
                return [i, n - i]

    def is_prime(self, n):
        if n < 2:
            return False

        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False

        return True

```

**Using Sieve**

```

class Solution:
    def sieve(self, N):
        # Generate isPrime List less equal than N
        isPrime = [1] * (N + 1);
        isPrime[0] = isPrime[1] = 0;
        # Sieve of Erastothenes
        for i in range(2, N + 1):
            if (isPrime[i] == 0):
                continue
            if (i > N // i): 
                break
            for j in range(i * i, N + 1, i):
                isPrime[j] = 0
        return isPrime

	def primesum(self, A):
        isPrime = self.sieve(A);
        ans = []
        for i in range(2, A + 1):
            if(isPrime[i] == 1 and isPrime[A - i] == 1):
                ans = [i, A - i]
                return ans
        return ans

```
