### Problem Description

Given an array of integers A, find and return the count of divisors of each element of the array.

NOTE: The order of the resultant array should be the same as the input array.



Problem Constraints
1 <= length of the array <= 100000
1 <= A[i] <= 106



Input Format
The only argument given is the integer array A.



Output Format
Return the count of divisors of each element of the array in the form of an array.



Example Input
Input 1:

 A = [2, 3, 4, 5]
Input 2:

 A = [8, 9, 10]


Example Output
Output 1:

 [2, 2, 3, 2]
Output 1:

 [4, 3, 4]


Example Explanation
Explanation 1:

 The number of divisors of 2 : [1, 2], 3 : [1, 3], 4 : [1, 2, 4], 5 : [1, 5]
 So the count will be [2, 2, 3, 2].
Explanation 2:

 The number of divisors of 8 : [1, 2, 4, 8], 9 : [1, 3, 9], 10 : [1, 2, 5, 10]
 So the count will be [4, 3, 4].
 
 
 
 **Solution Approach**
 
Using seive, we can store the smallest prime factor for all the numbers upto the maximum no (here it is 106).
This above information helps in determining the prime factors for any number in O(log n) time-complexity for each query.

We take each no in the input array. Then prime factorise it to count the powers of each prime factors in a number.

N = (p1n1) * (p2n2) * (p3n3).

Here, N can be represented as p1 prime raised to the power n1 muliply p2 prime raised to n2 multiply p3 raised to n3.

So, total factors of N will be (n1 + 1) * (n2 + 1) * (n3 + 1).

For eg: 18 = (21) * (32).

So, total factors = 2*3 = 6.

 ```
 
 class Solution:

    import math;
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

        result = [];
        for i in range(len(A)):
            num_divisors = self.helper(A[i],spf);
            result.append(num_divisors);
        
        return result;
    
    def helper(self,n,spf):

        total = 1;

        while n>1:
            prime = spf[n];
            count = 0;

            while n%prime == 0:
                count += 1;
                n = n//prime;

            total = total * (1+count)
        
        return total;
 
 ```
