### Problem Description

Given an array of positive integers A, check and return whether the array elements are consecutive or not.
NOTE: Try this with O(1) extra space.



Problem Constraints
1 <= length of the array <= 100000
1 <= A[i] <= 10^9



Input Format
The only argument given is the integer array A.



Output Format
Return 1 if the array elements are consecutive else return 0.



Example Input
Input 1:

 A = [3, 2, 1, 4, 5]
Input 2:

 A = [1, 3, 2, 5]


Example Output
Output 1:

 1
Output 2:

 0


Example Explanation
Explanation 1:

 As you can see all the elements are consecutive, so we return 1.
Explanation 2:

 Element 4 is missing, so we return 0.

**Using Extra Space**

```

class Solution:

    def solve(self, A):

        mini,maxi = A[0],A[0];
        st = set();

        for i in range(len(A)):

            st.add(A[i]);

            mini = min(mini,A[i]);
            maxi = max(maxi,A[i]);
        
        if len(A) != len(st):
            return 0;
        
        for i in range(mini+1,maxi):

            if i not in st:
                return 0;
        
        return 1;
        
```

**Approach**

We can check that if we sort the array in increasing order, the prev element should be less than the current one.

If this condition satisfies for the whole array, then we return 1 else, return 0.

NOTE: Array doesn’t need to start with 1.


```

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        n = len(A)
        # sort the given array
        A.sort()
        prev = 0
        # check if the elements are consecutive
        for i in range(n):
            if i == 0:
                prev = A[i]
            elif prev + 1 != A[i]:
                return 0
            prev = A[i]
        return 1

```
