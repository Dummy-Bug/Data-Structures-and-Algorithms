### Problem Description

The Fibonacci numbers are the numbers in the following integer sequence.

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ……..

In mathematical terms, the sequence Fn of Fibonacci numbers is defined by the recurrence relation:

Fn = Fn-1 + Fn-2

Given a number A, find and return the Ath Fibonacci Number.

Given that F0 = 0 and F1 = 1.



Problem Constraints
0 <= A <= 20



Input Format
First and only argument is an integer A.



Output Format
Return an integer denoting the Ath term of the sequence.



Example Input
Input 1:

 A = 2
Input 2:

 A = 9


Example Output
Output 1:

 1
Output 2:

 34


Example Explanation
Explanation 1:

 f(2) = f(1) + f(0) = 1
Explanation 2:

 f(9) = f(8) + f(7) = 21 + 13  = 34
 
 **Approach**
 Use recursion to apply the formula. Do not forget to add base cases or else you might run into an infinite loop.

Time Complexity: T(n) = T(n-1) + T(n-2) which is exponential.
We can observe that this implementation does a lot of repeated work (see the following recursion tree). 
So this is a bad implementation for nth Fibonacci number.

                       fib(5)   
                     /                \
               fib(4)                fib(3)   
             /        \              /       \ 
         fib(3)      fib(2)         fib(2)   fib(1)
        /    \       /    \        /      \
  fib(2)   fib(1)  fib(1) fib(0) fib(1) fib(0)
  /     \
fib(1) fib(0)
Extra Space: O(n) if we consider the function call stack size, otherwise O(1).
 
 ```
 
 class Solution:

    def findAthFibonacci(self, A):

        if A == 0 or A == 1:
            return A;
        
        return self.findAthFibonacci(A-1)+self.findAthFibonacci(A-2);

 
 ```
