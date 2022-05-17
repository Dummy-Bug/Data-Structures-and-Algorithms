# https://leetcode.com/problems/trapping-rain-water/

class Solution:
    def trap(self, height: List[int]) -> int:
        
        if len(height) < 3:
            return 0
        
        left  = 0 ; left_max = 0
        
        right = len(height)-1 ; right_max = 0
        
        water_trapped = 0
        
        while left < right:
            
            if height[left] <= height[right] :# Then try to calculate traped water from left side
                
                if height[left] >= left_max: # True then we have current element as the maximum
                    left_max = height[left]  # Hence cannot store water
                    
                else:
                    water_trapped += left_max - height[left]
                    
                left += 1
            
            else: # Then try to find trapped water from right side
                
                if height[right] >= right_max:
                    right_max = height[right]
                
                else:
                    water_trapped += right_max - height[right]
                
                right -= 1
        
        return water_trapped

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
                
                    
                    