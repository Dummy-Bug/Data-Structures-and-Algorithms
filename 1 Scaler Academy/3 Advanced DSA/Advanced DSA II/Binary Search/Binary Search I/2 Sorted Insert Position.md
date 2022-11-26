### Problem Description

Given a sorted array A of size N and a target value B, return the index (0-based indexing) if the target is found.
If not, return the index where it would be if it were inserted in order.

NOTE: You may assume no duplicates in the array. Users are expected to solve this in O(log(N)) time.



Problem Constraints
1 <= N <= 106



Input Format
The first argument is an integer array A of size N.
The second argument is an integer B.



Output Format
Return an integer denoting the index of target value.



Example Input
Input 1:

A = [1, 3, 5, 6]
B = 5 
Input 2:

A = [1]
B = 1


Example Output
Output 1:

2 
Output 2:

0


Example Explanation
Explanation 1:

The target value is present at index 2. 
Explanation 2:

The target value is present at index 0.


```

class Solution:
    
    def searchInsert(self, A, B):
        import bisect
        # LowerBound >= k; # UpperBound > K;
        # bisect_left is LowerBound
        
        return bisect.bisect_left(A,B);

```

```

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def searchInsert(self, A, B):
        n = len(A)
        low = 0
        high = n - 1
        while low <= high:
            mid = (low + high) / 2
            mid = int(mid)
            if A[mid] == B:
                return mid
            elif A[mid] < B:
                low = mid + 1
            else:
                high = mid - 1
        return low

```
