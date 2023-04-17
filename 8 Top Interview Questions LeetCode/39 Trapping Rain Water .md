### Problem Description 

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

 

Example 1:


Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9
 

Constraints:

n == height.length
1 <= n <= 2 * 104
0 <= height[i] <= 105


```
class Solution:
    def trap(self, height: List[int]) -> int:
        
        if len(height) < 3:
            return 0
        
        water_traped = 0
        
        # using two pointers i and j on indices 1 and n-1
        left  = 0
        right = len(height) - 1
        
        #initialising leftmax to the leftmost bar and rightmax to the rightmost bar
        left_max  = height[0]
        right_max = height[-1]
        
        while left < right:
            # check lmax and rmax for current i, j positions
            
            if height[left] > left_max:
                left_max = height[left]
                
            if height[right] > right_max:
                right_max = height[right]
            
            # fill water upto lmax level for index i and move i to the right
            if left_max <= right_max:
                water_traped += left_max - height[left]
                left += 1
				
            # fill water upto rmax level for index j and move j to the left
            else:
                water_traped += right_max - height[right]
                right -= 1
                
        return water_traped

```

**Using Two pointers to be Done**
