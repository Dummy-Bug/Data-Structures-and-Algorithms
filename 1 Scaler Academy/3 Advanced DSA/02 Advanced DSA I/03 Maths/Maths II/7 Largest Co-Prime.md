
Problem Description

You are given two positive numbers A and B . You need to find the maximum valued integer X such that:

X divides A i.e. A % X = 0
X and B are co-prime i.e. gcd(X, B) = 1


Problem Constraints

1 <= A, B <= 109



Input Format

First argument is an integer A.
Second argument is an integer B.



Output Format

Return an integer maximum value of X as descibed above.



Example Input

Input 1:

 A = 30
 B = 12
Input 2:

 A = 5
 B = 10


Example Output

Output 1:

 5
Output 2:

 1


Example Explanation

Explanation 1:

 All divisors of A are (1, 2, 3, 5, 6, 10, 15, 30). 
 The maximum value is 5 such that A%5 == 0 and gcd(5,12) = 1
Explanation 2:

 1 is the only value such that A%5 == 0 and gcd(1,10) = 1
 
 
https://www.youtube.com/watch?v=tZ7ISzMAYds 

**Solution Appproach**

We can try to remove the common factors of A and B from A by finding the greatest common divisor (gcd) of A and B and dividing A with that gcd.

Mathematically, A = A / gcd(A, B) —— STEP1
Now, we repeat STEP1 till we get gcd(A, B) = 1.
Atlast, we return X = A

How does this work ?

On doing prime factorization of A and B, we get :

A = p1x1 . p2x2 . … . pkxk
B = q1y1 . q2y2 . … . qlyl
Where pi ; i = 1, 2, …, k are prime factors of A and xi ; i = 1, 2, …, k are their respective powers
Similarly, qj ; i = 1, 2, …, l are prime factors of B and yi ; j = 1, 2, …, l are their respective powers

Let ri ; i = 1, 2, …, m be the common factors of A and B. By repeating STEP1, we are reducing the respective powers of ri by at least one each 
time (Proof of this is left to the reader). Therefore, we reach a point where powers of ri become zero, and the product of the rest prime-powers 
in A form the largest divisor of A that is co-prime with B.

**Removing Common Factors one by one**

```

class Solution:
	def cpFact(self, A, B):
        while(self.gcd(A, B) != 1):
            A = A // self.gcd(A, B)
        return A   ;
    
    def gcd(self,A,B):
        if B==0:
            return A;
        return self.gcd(B,A%B);

```
