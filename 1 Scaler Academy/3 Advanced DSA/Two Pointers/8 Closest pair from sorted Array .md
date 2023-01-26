### Problem Description

Given two sorted arrays of distinct integers, A and B, and an integer C, find and return the pair whose sum is closest to C and the pair has one element from each array.

More formally, find A[i] and B[j] such that abs((A[i] + B[j]) - C) has minimum value.

If there are multiple solutions find the one with minimum i and even if there are multiple values of j for the same i then return the one with minimum j.

Return an array with two elements {A[i], B[j]}.



Problem Constraints

1 <= length of both the arrays <= 100000

1 <= A[i], B[i] <= 109

1 <= C <= 109



Input Format

The first argument given is the integer array A.
The second argument given is the integer array B.
The third argument given is integer C.



Output Format

Return an array of size 2 denoting the pair which has sum closest to C.



Example Input

Input 1:

 A = [1, 2, 3, 4, 5]
 B = [2, 4, 6, 8]
 C = 9
Input 2:

 A = [5, 10, 20]
 B = [1, 2, 30]
 C = 13


Example Output

Output 1:

 [1, 8]
Output 2:

 [10, 2]


Example Explanation

Explanation 1:

 There are three pairs: (1, 8), (3, 6), (5, 4), that gives the minimum value.
 Since we have to return the value with minimum i and then with minimum j. We will return [1, 8].
Explanation 2:

 [10, 2] is the only pair such abs(10+2-13) is minimum.
 
 **Approach**
 
 This problem can be solved by using two pointer approach.

Let say l = 0 i.e. it point at the start of array A and r = len(B) - 1 i.e. it points to end of array B.
Also maintain a variable, let say, dif, which stores the minimum of abs(A[i]+B[j]-C).

Now, If abs(A[l]+B[r]-C) < dif then update the value of dif and the value of two A[i] and A[j] and there indices.

If abs(A[l]+B[r]-C) == dif then we need to update the indixes such that l and r are minimum as possible in case of multiple solution.

Also, increment l and decrement r accordingly.

```


class Solution:

    def solve(self, A, B, C):

        p1 = 0; closest_sum = float('inf');
        p2 = len(B)-1; ans = [None,None];

        while p1<len(A) and p2>-1:
            
            curr_sum = A[p1] + B[p2];

            if closest_sum > abs(curr_sum-C):

                closest_sum = abs(curr_sum-C);
                left_index  = p1; right_index = p2;

            if closest_sum == abs(curr_sum-C) and p1 <= left_index and p2<=right_index:
                left_index  = p1;
                right_index = p2;

            if curr_sum > C:
                p2 -= 1;
            else:
                p1 += 1;
        
        return [A[left_index],B[right_index]];
            
            
```
