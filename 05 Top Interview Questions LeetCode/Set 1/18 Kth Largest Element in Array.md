### Problem Description

Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

You must solve it in O(n) time complexity.

 

Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
Example 2:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
 

Constraints:

1 <= k <= nums.length <= 105
-104 <= nums[i] <= 104


```

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        self.k = k-1;
        return self.helper(nums,0,len(nums)-1);
        
    
    def helper(self,nums,start,end):
        
        while start <= end:
            
            pivot_index = self.partition(nums,start,end);
            # print(pivot_index)
            if pivot_index == self.k:
                return nums[pivot_index];
            
            elif pivot_index > self.k:
                return self.helper(nums,start,pivot_index-1);
            else:
                return self.helper(nums,pivot_index+1,end);
    
    def partition(self,nums,start,end):
        
        pivot_index = start;
        left = start+1; right = end;
        # conditions for kth largest and kth smallest would be different   
        while left<=right:
            
            if nums[left] > nums[pivot_index]:
                left += 1;
            
            elif nums[right] <= nums[pivot_index]:
                right -= 1;
            else:
                nums[left],nums[right] = nums[right],nums[left];
                left  += 1;
                right -=1 
        
        nums[pivot_index],nums[left-1] = nums[left-1],nums[pivot_index];
        
        return left-1;
        

```
