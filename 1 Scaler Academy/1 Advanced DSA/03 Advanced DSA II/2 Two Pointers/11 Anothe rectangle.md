### Problem Description

Given a sorted array of distinct integers A and an integer B, find and return how many rectangles with distinct configurations can be created using elements of this array as length and breadth whose area is lesser than B.

(Note that a rectangle of 2 x 3 is different from 3 x 2 if we take configuration into view)



Problem Constraints

1 <= |A| <= 100000
1 <= A[i] <= 109
1 <= B <= 109



Input Format

The first argument given is the integer array A.

The second argument given is integer B.



Output Format

Return the number of rectangles with distinct configurations with area less than B modulo (109 + 7).



Example Input

Input 1:

 A = [1, 2]
 B = 5
Input 2:

 A = [1, 2]
 B = 1


Example Output

Output 1:

 4
Output 2:

 0


Example Explanation

Explanation 1:

 All 1X1, 2X2, 1X2 and 2X1 have area less than 5.
Explanation 2:

 No Rectangle is valid.
 
 
 **Approach**
 
 2 pointer technique is absolutely valid here.
We would like to consider every length and breadth and calculate it.
You can create two pointers l and r out of which initially one will point to index 0 and
another will point to last index of the array and it the rectangle formed by them is
valid the include all possible rectangles with A[l] and A[r] as length or breadth of reactangle.

```

class Solution:

    def solve(self, A, B):

        rectangle_count = 0; mod = 1000000000+7;
        p1 = 0; p2 = len(A)-1;

        while p1<=p2:
            
            area    = A[p1]*A[p2];

            if area >= B:
                p2 -=1;
            else:
                rectangle_count = ( (rectangle_count)%mod + (2*(p2-p1))%mod + 1 )%mod;
                p1 += 1;
        
        return rectangle_count;




```
