### Problem Description

Farmer John has built a new long barn with N stalls. Given an array of integers A of size N where each element of the array represents the location
of the stall and an integer B which represents the number of cows.

His cows don't like this barn layout and become aggressive towards each other once put into a stall. To prevent the cows from hurting each other, 
John wants to assign the cows to the stalls, such that the minimum distance between any two of them is as large as possible. What is the largest 
minimum distance?



Problem Constraints
2 <= N <= 100000
0 <= A[i] <= 109
2 <= B <= N



Input Format
The first argument given is the integer array A.
The second argument given is the integer B.



Output Format
Return the largest minimum distance possible among the cows.



Example Input
Input 1:

A = [1, 2, 3, 4, 5]
B = 3
Input 2:

A = [1, 2]
B = 2


Example Output
Output 1:

 2
Output 2:

 1


Example Explanation
Explanation 1:

 John can assign the stalls at location 1, 3 and 5 to the 3 cows respectively. So the minimum distance will be 2.
Explanation 2:

 The minimum distance will be 1.
 
 ```
 
 class Solution:

    def solve(self, A, B):
        
        A.sort();
    
        low = float('inf');

        for i in range(1,len(A)):
            low = min(low,A[i]-A[i-1]);
        n = len(A);
        high = A[n-1] - A[0];
        
        maximum_distance = 0;
       
        while low <= high:

            mid = (low+high)//2;
            
            if self.can_place_cow(A,mid,B):
                
                maximum_distance = mid;
                low = mid + 1;
            else:
                high = mid - 1;

        return maximum_distance;

    def can_place_cow(self,A,max_distance,B):
        
        num_cows = 1;
        curr_distance = 0;
        prev_cow_pos  = A[0];

        for i in range(1,len(A)):

            curr_distance = A[i] - prev_cow_pos;

            if curr_distance >= max_distance:
                num_cows += 1;
                prev_cow_pos = A[i];
                curr_distance = A[i] - prev_cow_pos;

            if num_cows >= B:
                return True;
        
        return False;

 ```
