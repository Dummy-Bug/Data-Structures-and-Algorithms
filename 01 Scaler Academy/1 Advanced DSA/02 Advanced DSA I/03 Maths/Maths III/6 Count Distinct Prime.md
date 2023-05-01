### Problem Description

You have given an array A having N integers. Let say G is the product of all elements of A.

You have to find the number of distinct prime divisors of G.



Input Format

The first argument given is an Array A, having N integers.
Output Format

Return an Integer, i.e number of distinct prime divisors of G.
Constraints

1 <= N <= 1e5
1 <= A[i] <= 1e5
For Example

Input:
    A = [1, 2, 3, 4]
Output:
     2

Explanation:
    here G = 1 * 2 * 3 * 4 = 24
    and distinct prime divisors of G are [2, 3]


**Approach**

You just have to find the prime divisors of each element of an array and count the distinct prime divisors.
You can use any data structure like set to store distinct elements.

```

class Solution:

    def solve(self, A):
        spf = [];

        for i in range(max(A) + 1):
            spf.append(i)
        
        for i in range(2,int(math.pow(len(spf),0.5)+1)):

            if spf[i] == i:

                j = i*i;
                while j < len(spf):
                    if spf[j] == j:
                        spf[j] = i;
                    j = j + i; 

        result = dict();
        for i in range(len(A)):
            self.helper(A[i],spf,result);
            
        return len(result.keys());
    
    def helper(self,n,spf,result):

        while n>1:
            prime = spf[n];
            
            if prime not in result:
                result[prime] = True;

            while (n%prime) == 0:
                n = n//prime;

```
