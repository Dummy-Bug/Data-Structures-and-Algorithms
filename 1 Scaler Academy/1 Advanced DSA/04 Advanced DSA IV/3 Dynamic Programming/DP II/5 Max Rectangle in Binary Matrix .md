### Problem Description

Given a 2-D binary matrix A of size N x M filled with 0's and 1's, find the largest rectangle containing only ones and return its area.



Problem Constraints
1 <= N, M <= 100



Input Format
The first argument is a 2-D binary array A.



Output Format
Return an integer denoting the area of the largest rectangle containing only ones.



Example Input
Input 1:

 A = [
       [1, 1, 1]
       [0, 1, 1]
       [1, 0, 0] 
     ]
Input 2:

 A = [
       [0, 1, 0]
       [1, 1, 1]
     ] 


Example Output
Output 1:

 4
Output 2:

 3


Example Explanation
Explanation 1:

 As the max area rectangle is created by the 2x2 rectangle created by (0, 1), (0, 2), (1, 1) and (1, 2).
Explanation 2:

 As the max area rectangle is created by the 1x3 rectangle created by (1, 0), (1, 1) and (1, 2).


```


class Solution:

    def largestRectangleArea(self, heights):

        N = len(heights)
        lefmin = []
        stack  = []
        for i in range(N):
            cur_val = heights[i]
            while stack and cur_val <= heights[stack[-1]]:
                stack.pop()
            if stack:
                lefmin.append(stack[-1] + 1)
            else:
                lefmin.append(0)
            stack.append(i)
            
        rightmin = []
        rstack    = []
        for i in range(N-1,-1,-1):
            cur_val = heights[i]
            while rstack and cur_val <= heights[rstack[-1]]:
                rstack.pop()
            if rstack:
                rightmin.append(rstack[-1] - 1)
            else:
                rightmin.append(N - 1)
            rstack.append(i)
            
        rightmin = rightmin[::-1]
        ans = float('-inf')
        
        for cur in range(N):
            length = (rightmin[cur] - lefmin[cur] + 1)
            ans    = max(ans,heights[cur] * length)
            
        return ans ;

	def maximalRectangle(self, A):
        rows = len(A);cols = len(A[0])
        ans = [0] * cols
        res = float('-inf')
        for i in range(rows):
            for j in range(cols):
                if A[i][j] == 1: 
                    ans[j] += 1
                else: 
                    ans[j] = 0
            value = self.largestRectangleArea(ans)
            res = max(res,value)
        return res
        
        
```
