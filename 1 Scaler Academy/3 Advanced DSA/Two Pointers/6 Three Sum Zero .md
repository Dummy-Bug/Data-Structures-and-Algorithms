### Problem Description

Given an array A of N integers, are there elements a, b, c in S such that a + b + c = 0

Find all unique triplets in the array which gives the sum of zero.

Note:

Elements in a triplet (a,b,c) must be in non-descending order. (ie, a ≤ b ≤ c) The solution set must not contain duplicate triplets.



Problem Constraints

0 <= N <= 7000

-108 <= A[i] <= 108



Input Format

Single argument representing a 1-D array A.



Output Format

Output a 2-D vector where each row represent a unique triplet.



Example Input

A = [-1,0,1,2,-1,4]


Example Output

[ [-1,0,1],
  [-1,-1,2] ]


Example Explanation

Out of all the possible triplets having total sum zero,only the above two triplets are unique.

**Solution Approach**

Make sure you are not processing the same triplets again.

Skip over the duplicates in the array.

Try a input like :
-1 -1 -1 -1 0 0 0 0 1 1 1 1
Ideally, you should get only 2 pairs : {[-1 0 1], [0 0 0]}


```

class Solution:

	def threeSum(self, A):

        triplets = [];
        A.sort();

        for i in range(len(A)-2):

            if i!= 0 and A[i] == A[i-1]:
                continue;
            
            p1,p2 = i+1,len(A)-1;

            while p1<p2:

                x,y,z = A[p1],A[p2],-1*A[i];

                curr_sum = x+y;

                if curr_sum > z:
                    p2 -= 1;
                elif curr_sum < z:
                    p1 += 1;
                else:
                    triplets.append([ A[i],A[p1],A[p2] ]);

                    while p1<p2 and A[p1] == x:
                        p1 += 1;
                    while p1<p2 and A[p2] == y:
                        p2 -= 1;

        return triplets;



```
