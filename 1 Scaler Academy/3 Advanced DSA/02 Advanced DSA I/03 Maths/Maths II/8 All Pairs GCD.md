### Problem Description

Given an array of integers A of size N containing GCD of every possible pair of elements of another array.

Find and return the original numbers used to calculate the GCD array in any order. For example, if original numbers are {2, 8, 10} then the given array will be {2, 2, 2, 2, 8, 2, 2, 2, 10}.



Problem Constraints
1 <= N <= 10000

1 <= A[i] <= 109



Input Format
The first and only argument given is the integer array A.



Output Format
Find and return the original numbers which are used to calculate the GCD array in any order.



Example Input
Input 1:

 A = [2, 2, 2, 2, 8, 2, 2, 2, 10]
Input 2:

 A = [5, 5, 5, 15]


Example Output
Output 1:

 [2, 8, 10]
Output 2:

 [5, 15]


Example Explanation
Explanation 1:

 Initially, array A = [2, 2, 2, 2, 8, 2, 2, 2, 10].
 2 is the gcd between 2 and 8, 2 and 10.
 8 and 10 are the gcds pair with itself.
 Therefore, [2, 8, 10] is the original array.
Explanation 2:

 Initially, array A = [5, 5, 5, 15].
 5 is the gcd between 5 and 15.
 15 is the gcds pair with itself.
 Therefore, [5, 15] is the original array.
 
 **Solution Approach**
 
 Draw the Matrix and you will observe that diagonal elements are the ones we want to find.
 
 Sort the array in decreasing order.
Highest element will always be one of the original numbers. Keep that number and remove it from the array.
Compute GCD of the element taken in the previous step with the current element starting from the greatest 
and discard the GCD value from the given array.

```

def GCD(a, b):
    if a == 0:
        return b
    return GCD(b % a, a)

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        A.sort(reverse = True)
        n = len(A)
        vec = []
        cnt = {}
        # cnt stores the count of A[i]'s that are to be deleted from the array
        for i in range(n):
            if (cnt.get(A[i]) != None and cnt[A[i]] > 0):
                cnt[A[i]] = cnt[A[i]] - 1
            else:
                for j in range(len(vec)):
                    gcd = GCD(vec[j], A[i]);
                    if cnt.get(gcd) == None:
                        cnt[gcd] = 2
                    else: 
                        cnt[gcd] = cnt[gcd] + 2
                    # we are adding 2 to the cnt as there will 2 pairs gcd(vec[j],A[i]) and gcd(A[i],vec[j])
                vec.append(A[i])
        return vec

```
