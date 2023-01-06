### Problem Description

Given three integers A, B, and C, where A represents n, B represents r, and C represents m, find and return the value of nCr % m where 
nCr % m = (n!/((n-r)!*r!))% m.

x! means factorial of x i.e. x! = 1 * 2 * 3... * x.



Problem Constraints
1 <= A * B <= 106

1 <= B <= A

1 <= C <= 106



Input Format
The first argument given is integer A ( = n).
The second argument given is integer B ( = r).
The third argument given is integer C ( = m).


Output Format
Return the value of nCr % m.



Example Input
Input 1:

 A = 5
 B = 2
 C = 13
Input 2:

 A = 6
 B = 2
 C = 13


Example Output
Output 1:

 10
Output 2:

 2


Example Explanation
Explanation 1:

 The value of 5C2 % 11 is 10.
Explanation 2:

 The value of 6C2 % 13 is 2.
 
 **Approach**
 
Suppose we calculate nCr by calculating the factorial of each number and then doing n! / (r! * (n-r)!) % m. 
This will not work as the factorial can be very large and will cause overflow.

As we know nCr = n-1Cr-1 + n-1Cr.

So we will use the Dynamic Programming approach and calculate the value of nCr.
 
 ```
 
 class Solution:

    def solve(self, A, B, C):

        dp = [[0 for j in range(B+1)] for i in range(A+1)];

        for i in range(len(dp)):
            for j in range(len(dp[0])):

                if j == 0:
                    dp[i][0] = 1;
                    continue;
                    
                if i == 0:
                    dp[0][j] = 0;
                    continue;

                dp[i][j] = (dp[i-1][j-1] + dp[i-1][j])%(C);
        
        return dp[A][B];
                
 
 ```
