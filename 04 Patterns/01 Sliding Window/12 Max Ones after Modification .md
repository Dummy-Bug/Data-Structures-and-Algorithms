### Problem Description

Given a binary array A and a number B, we need to find length of the longest subsegment of ‘1’s possible by changing at most B ‘0’s.



Problem Constraints
 1 <= N, B <= 105

 A[i]=0 or A[i]=1



Input Format
First argument is an binary array A.

Second argument is an integer B.



Output Format
Return a single integer denoting the length of the longest subsegment of ‘1’s possible by changing at most B ‘0’s.



Example Input
Input 1:

 A = [1, 0, 0, 1, 1, 0, 1]
 B = 1
Input 2:

 A = [1, 0, 0, 1, 0, 1, 0, 1, 0, 1]
 B = 2


Example Output
Output 1:

 4
Output 2:

 5


Example Explanation
Explanation 1:

 Here, we should only change 1 zero(0). Maximum possible length we can get is by changing the 3rd zero in the array,
 we get a[] = {1, 0, 0, 1, 1, 1, 1}
Explanation 2:

 Here, we can change only 2 zeros. Maximum possible length we can get is by changing the 3rd and 4th (or) 4th and 5th zeros.
 
 
 ```
 
 class Solution:

    def solve(self, A, B):
        
        longest_segment_length = 0;
        zero_count = 0;
        
        p1 = p2 = 0;
        
        while (p2<len(A)):
            
            if A[p2] == 0:
                zero_count += 1;
            
            if zero_count <= B:
                longest_segment_length = max(p2-p1+1,longest_segment_length);
                p2 += 1;
                
            else:
                while zero_count>B:
                    if A[p1] == 0:
                        zero_count -= 1;
                    p1 += 1;
                
                p2 += 1;
        
        return longest_segment_length;
 
 ```
