### Problem Description

Given two integers A and B, find a number X such that A xor X is minimum possible, and the number of set bits in X equals B.



Problem Constraints
0 <= A <= 109
0 <= B <= 30



Input Format
First argument contains a single integer A. Second argument contains a single integer B.



Output Format
Return a single integer X.



Example Input
Input 1:

 A = 3
 B = 3
Input 2:

 A = 15
 B = 2


Example Output
Output 1:

 7
Output 2:

 12


Example Explanation
Explanation 1:

 3 xor 7 = 4 which is minimum
Explanation 2:

 15 xor 12 = 3 which is minimum
 
 **Solution Approach**
 
 Let X initially be 0
First try to set those bits which contribute the highest(right side) 
while count of set bits in X is less than B. Then Set all zero bits from left side.
 
 ```
 
 class Solution:

    def solve(self, A, B):
        # B is the number of setBits
        setBits = B; ans = 0;

        for i in range(31,-1,-1):

            if self.CheckBits(A,i):

                if setBits != 0:
                    ans = ans + (1<<i);
                    setBits -= 1
                else:
                    return ans;
        if setBits <= 0:
            return ans;
        for i in range(32):

            if setBits > 0:
                if self.CheckBits(ans,i) == False:
                    # print(ans,i,setBits,1<<i)
                    ans = ans + (1<<i);
                    
                    setBits -=1 
            else:
                return ans;

    def CheckBits(self,n,i):

        if (n>>i)&1 == 1:
            return True;
        
        return False;
 
 ```
