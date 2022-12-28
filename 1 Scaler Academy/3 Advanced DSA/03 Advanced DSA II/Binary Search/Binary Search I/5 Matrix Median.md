### Problem Description

Given a matrix of integers A of size N x M in which each row is sorted.

Find and return the overall median of matrix A.

NOTE: No extra memory is allowed.

NOTE: Rows are numbered from top to bottom and columns are numbered from left to right.



Problem Constraints
1 <= N, M <= 10^5

1 <= N*M <= 10^6

1 <= A[i] <= 10^9

N*M is odd



Input Format
The first and only argument given is the integer matrix A.



Output Format
Return the overall median of matrix A.



Example Input
Input 1:

A = [   [1, 3, 5],
        [2, 6, 9],
        [3, 6, 9]   ] 
Input 2:

A = [   [5, 17, 100]    ]


Example Output
Output 1:

 5 
Output 2:

 17


Example Explanation
Explanation 1:

A = [1, 2, 3, 3, 5, 6, 6, 9, 9]
Median is 5. So, we return 5. 
Explanation 2:

Median is 17.

**Solution Approach**

-> We cannot use extra memory, so we can’t store all elements in an array and sort the array.
  But since rows are sorted, it must be of some use, right?

  Note that in a row, you can binary search to find how many elements are smaller than a value X in O(log M).
  This is the base of our solution.

  Say k = N*M/2. We need to find (k + 1)^th smallest element.
  We can use binary search on the answer. In O(N log M), we can count how many elements are smaller than X in the matrix.

  So, we use binary search on the interval [1, INT_MAX]. So, the total complexity is O(30 * N log M).

 Note:
  This problem can be solved by using a min-heap, but extra memory is not allowed.

```

class Solution:

	def matrix_search(self,A,B):
		
		num_ele = 0;
		
		for row in range(len(A)):

			low  = 0; high = len(A[0])-1;
			index = -1;
			
			while low <= high:
				
				mid = (low+high)//2;
				
				if A[row][mid] < B:
					index = mid;
					low   = mid + 1;
				else:
					high = mid - 1;
			
			num_ele += (index+1);
		
		return num_ele;
				
		
	def findMedian(self, A):
		
		low = float('inf');
		for i in range(len(A)):
			low = min(low,A[i][0]);
		
		high = float('-inf');
		for i in range(len(A)):
			high = max(high,A[i][-1]);
			
		median = -1;
		n = (len(A)*len(A[0]))//2;
		
		while low <= high:
			
			mid = low + (high-low)//2;
			ans = self.matrix_search(A,mid);

			if ans <= n:
				median = mid;
				low = mid + 1
			if ans > n:
				high = mid - 1
		
		return median;


```
