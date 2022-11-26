Given an array of integers A, find and return the peak element in it. An array element is peak if it is NOT smaller than its neighbors.

For corner elements, we need to consider only one neighbor. We ensure that answer will be unique.

NOTE: Users are expected to solve this in O(log(N)) time. The array may have duplicate elements.



Problem Constraints
1 <= |A| <= 100000

1 <= A[i] <= 109



Input Format
The only argument given is the integer array A.



Output Format
Return the peak element.



Example Input
Input 1:

A = [1, 2, 3, 4, 5]
Input 2:

A = [5, 17, 100, 11]


Example Output
Output 1:

 5
Output 2:

 100


Example Explanation
Explanation 1:

 5 is the peak.
Explanation 2:

 100 is the peak.


**Solution Approach**

```

class Solution:

    def solve(self, A):

        if len(A) == 1:
            return A[0]
        if len(A) == 2:
            return max(A[0],A[1])
        low  = 0;
        high = len(A)-1;

        while low <= high:

            mid = low + (high-low)//2;
            # print(mid,A[mid]);

            if mid == 0:

                if A[mid] >= A[mid+1]:
                    return A[mid];
                else:
                    return -1

            if mid == len(A)-1:

                if A[mid] >= A[mid-1]:
                    return A[mid];
                else:
                    return -1
            if A[mid-1] <= A[mid] >= A[mid+1]:
                return A[mid];
            if A[mid] < A[mid+1]:
                low = mid + 1;
            else:
                high = mid - 1;
        
        return -1

```
