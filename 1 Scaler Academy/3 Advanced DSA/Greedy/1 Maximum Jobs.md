### Problem Description

There are N jobs to be done, but you can do only one job at a time.

Given an array A denoting the start time of the jobs and an array B denoting the finish time of the jobs.

Your aim is to select jobs in such a way so that you can finish the maximum number of jobs.

Return the maximum number of jobs you can finish.



Problem Constraints
1 <= N <= 105

1 <= A[i] < B[i] <= 109



Input Format
The first argument is an integer array A of size N, denoting the start time of the jobs.
The second argument is an integer array B of size N, denoting the finish time of the jobs.



Output Format
Return an integer denoting the maximum number of jobs you can finish.



Example Input
Input 1:

 A = [1, 5, 7, 1]
 B = [7, 8, 8, 8]
Input 2:

 A = [3, 2, 6]
 B = [9, 8, 9]


Example Output
Output 1:

 2
Output 2:

 1


Example Explanation
Explanation 1:

 We can finish the job in the period of time: (1, 7) and (7, 8).
Explanation 2:

 Since all three jobs collide with each other. We can do only 1 job.
 
 
 ```
 
 class Solution:
    
    def solve(self, A, B):

        temp_arr = [];
        for i in range(len(A)):
            temp_arr.append([B[i],A[i]]);
        
        temp_arr.sort();
        result = 0; prev_finish = 0;

        for i in range(len(temp_arr)):

            curr_finish = temp_arr[i][0];
            curr_start  = temp_arr[i][1];

            if curr_start >= prev_finish:
                prev_finish = curr_finish;
                result += 1;
        return result;
        
 
 ```
