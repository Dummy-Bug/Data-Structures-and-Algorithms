### Problem Description

A lucky number is a number that has exactly 2 distinct prime divisors.

You are given a number A, and you need to determine the count of lucky numbers between the range 1 to A (both inclusive).



Problem Constraints
1 <= A <= 50000



Input Format
The first and only argument is an integer A.



Output Format
Return an integer i.e the count of lucky numbers between 1 and A, both inclusive.



Example Input
Input 1:

 A = 8
Input 2:

 A = 12


Example Output
Output 1:

 1
Output 2:

 3


Example Explanation
Explanation 1:

 Between [1, 8] there is only 1 lucky number i.e 6.
 6 has 2 distinct prime factors i.e 2 and 3.
Explanation 2:

 Between [1, 12] there are 3 lucky number: 6, 10 and 12.
 
 
 ```
 
 class Solution:

    import math;

    def solve(self, A):

        if A <= 3:
            return 0;

        spf = [];

        for i in range(A + 1):
            spf.append(i)
        
        for i in range(2,int(math.pow(A,0.5)+1)):

            if spf[i] == i:

                j = i*i;
                while j < len(spf):
                    if spf[j] == j:
                        spf[j] = i;
                    j = j + i; 

        result = 0;
        for i in range(4,A+1):
            result  = result + self.helper(i,spf);
        
        return result;
    
    def helper(self,n,spf):

        count = 0;

        while n>1:
            prime = spf[n];
            count += 1
            if count > 2:
                return 0;

            while (n%prime) == 0:
                n = n//prime;

        if count < 2:
            return 0
        return 1;
 
 ```
