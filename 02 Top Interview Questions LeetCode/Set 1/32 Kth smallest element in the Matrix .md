### Problem Description 

Given an n x n matrix where each of the rows and columns is sorted in ascending order, return the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

You must find a solution with a memory complexity better than O(n2).

 

Example 1:

Input: matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
Output: 13
Explanation: The elements in the matrix are [1,5,9,10,11,12,13,13,15], and the 8th smallest number is 13
Example 2:

Input: matrix = [[-5]], k = 1
Output: -5
 

Constraints:

n == matrix.length == matrix[i].length
1 <= n <= 300
-109 <= matrix[i][j] <= 109
All the rows and columns of matrix are guaranteed to be sorted in non-decreasing order.
1 <= k <= n2
 

Follow up:

Could you solve the problem with a constant memory (i.e., O(1) memory complexity)?
Could you solve the problem in O(n) time complexity? The solution may be too advanced for an 
interview but you may find reading this paper fun.


```

class Solution:
    def kthSmallest(self, A: List[List[int]], B: int) -> int:
        heap = []; flag = False;
        heapq.heapify(heap);

        for i in range(len(A)):
            for j in range(len(A[0])):
                
                if len(heap)<B:
                    heapq.heappush(heap,-1*A[i][j]);

                elif -1*heap[0] > A[i][j]:
                    heapq.heappop(heap);
                    heapq.heappush(heap,-1*A[i][j]);

        return -1*heapq.heappop(heap);

```

**Binary Search**


```


class Solution:  # 160 ms, faster than 93.06%
    def kthSmallest(self, matrix, k):
        m, n = len(matrix), len(matrix[0])  # For general, the matrix need not be a square

        def countLessOrEqual(x):
            cnt = 0
            c = n - 1  # start with the rightmost column
            for r in range(m):
                while c >= 0 and matrix[r][c] > x: c -= 1  # decrease column until matrix[r][c] <= x
                cnt += (c + 1)
            return cnt

        left, right = matrix[0][0], matrix[-1][-1]
        ans = -1
        while left <= right:
            mid = (left + right) // 2
            if countLessOrEqual(mid) >= k:
                ans = mid
                right = mid - 1  # try to looking for a smaller value in the left side
            else:
                left = mid + 1  # try to looking for a bigger value in the right side

        return ans
        
```
