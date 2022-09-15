###  Largest Rectangle in Histogram

https://leetcode.com/problems/largest-rectangle-in-histogram/


**Hint 1**

> What’s the brute force approach here?

  We know that the height of the largest rectangle will be one of the heights of the histogram bars (Think, why?)
  If that is the case, we can iterate on all the histogram bars, and for each histogram bar H, we try to create the maximum rectangle with H as the height.
  We keep going left L and right R until we encounter a histogram bar with a height less than H.
  Now, (R - L - 1) * H is one of the possibilities for the largest rectangle.

  Doing this for all the histogram bars will give us the right solution.

  Following is rough pseudocode for the approach mentioned above :


  max_rectangle = 0 

  for index = 0 to all_histograms.length
    H = all_histograms[index]
    L = index, R = index
    while L >= 0 AND all_histograms[L] >= H
      L = L - 1
    while R < all_histograms.length AND all_histograms[R] >= H
      R = R + 1
    max_rectangle = MAX(max_rectangle, (R - L - 1) * H)

  return max_rectangle


  This approach is, however, O(N^2) time complexity in the worst case. How can we do better than this approach?

  Hint: Think in terms of using a stack ?
  
 **Hint 2**
 
 > As discussed in the previous hint, the height of the maximum rectangle will be the height of one of the histogram bars. For each histogram H, we need to know the index of the first smaller (smaller than H) bar on the left of H (let’s call it L) and the index of the first smaller bar on the right of H.
We have already tried the brute force approach. How can we do better?

  Important observation:

  Lets consider 2 consecutive histogram bars H[i] and H[i+1]. Lets assume H[i+1] < H[i]
  In such a case, for all histogram bars X with index > i + 1 when traversing left for L, there is no point looking at H[i] after looking at H[i+1]. If H[i+1] > X, obviously H[i] > X as we already know H[i] > H[i+1]

  Then, what is the next entry we would want to look at? We want to look at the first histogram bar left of H[i+1] with a height less than H[i+1].

  Can you think of a stack-based approach based on the above observation?
  
  
  ```
  
from collections import deque;

class Solution:

	def largestRectangleArea(self, A):

		nsl = []; nsr = [];
		stack = deque([]);

		for i in range(len(A)):

			while stack and A[stack[-1]] >= A[i]:
				stack.pop();
			if not stack:
				nsl.append(-1);
			else:
				nsl.append(stack[-1]);
			stack.append(i);

		stack = deque([]);

		for i in range(len(A)-1,-1,-1):

			while stack and A[stack[-1]] >= A[i]:
				stack.pop();
			if not stack:
				nsr.append(len(A));
			else:
				nsr.append(stack[-1]);
			stack.append(i);

		nsr = nsr[::-1];
		max_area = 0;

		for i in range(len(A)):

			width = nsr[i]-nsl[i]-1;
			curr_area = A[i]*width;

			max_area = max(max_area,curr_area);
		
		return max_area;
  
  ```


