### Problem Description

Given an array A of size N, Groot wants you to pick 2 indices i and j such that

1 <= i, j <= N
A[i] % A[j] is maximum among all possible pairs of (i, j).
Help Groot in finding the maximum value of A[i] % A[j] for some i, j.



Problem Constraints
1 <= N <= 100000
0 <= A[i] <= 100000



Input Format
First and only argument in an integer array A.



Output Format
Return an integer denoting the maximum value of A[i] % A[j] for any valid i, j.



Example Input
Input 1:

 A = [1, 2, 44, 3]
Input 2:

 A = [2, 6, 4]


Example Output
Output 1:

 3
Output 2:

 4


Example Explanation
Explanation 1:

 For i = 3, j = 2  A[i] % A[j] = 3 % 44 = 3.
 No pair exists which has more value than 3.
Explanation 2:

 For i = 2, j = 1  A[i] % A[j] = 4 % 6 = 4.

**Approach**

Beware. The array can have duplicates as well.
In that case, it might be possible that the last two numbers of the sorted array are the same, in which case A[i]%A[j] will be 0
therefore to put it more formally, we have to take the largest and second-largest distinct number of the array, which need not be the 
last two elements
of the array.
This can be done by iterating over the sorted array.
If the array has only one distinct element, then no matter which pair you choose, the answer will always be 0.


```

class Solution:

    def solve(self, A):
        n = len(A)
        flag = 0
        # sort the array
        A.sort()
        # keep the pointer at the end of the array
        i = n - 1
        # keep going backwards until we dont find a different element
        while(flag == 0 and i != 0):
            if(A[i] == A[i-1]):
                i -= 1
            else:
                flag = 1
        # if we find a different element before reaching the end of the array, print the element at the index before that
        # else return 0 because in that case all the elements are same and no matter which indices we choose, the answer will always be 0
        if(i != 0):
            return A[i-1]
        else:
            return 0

```

```

class Solution:

    def solve(self, A):

        A.sort();

        mod = 0;

        for i in range(len(A)-1):

            if A[i+1] != 0:
                mod = max(mod,A[i]%A[i+1]);
        
        return mod;


```
