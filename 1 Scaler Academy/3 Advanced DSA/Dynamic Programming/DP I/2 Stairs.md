### Problem Description

You are climbing a staircase and it takes A steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Return the number of distinct ways modulo 1000000007



Problem Constraints
1 <= A <= 105



Input Format
The first and the only argument contains an integer A, the number of steps.



Output Format
Return an integer, representing the number of ways to reach the top.



Example Input
Input 1:

 A = 2
Input 2:

 A = 3


Example Output
Output 1:

 2
Output 2:

 3


Example Explanation
Explanation 1:

 Distinct ways to reach top: [1, 1], [2].
Explanation 2:

 Distinct ways to reach top: [1 1 1], [1 2], [2 1].
 
 
 
 ```
 
class Solution:
	# @param A : integer
	# @return an integer
	def climbStairs(self, val):

        temp_arr = [-1]*(val+1); mod = 1000000007;

        temp_arr[0] = 1; temp_arr[1] = 2;

        for i in range(2,len(temp_arr)):
            temp_arr[i] = ( temp_arr[i-1] + temp_arr[i-2] )%mod;
        
        return temp_arr[val-1];



 
 ```
