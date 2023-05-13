### Problem Description 

There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
Example 3:

Input: nums = [1], target = 0
Output: -1
 

Constraints:

1 <= nums.length <= 5000
-104 <= nums[i] <= 104
All values of nums are unique.
nums is an ascending array that is possibly rotated.
-104 <= target <= 104



```

class Solution:
    def getPivot(self,nums):
        low = 0
        hi  = len(nums)-1
        while low <= hi:
            mid = (low+hi)//2
            
            if nums[mid] >= nums[low] and nums[mid] <= nums[hi]:
                return low
            else: # iske andar nums[low] would be > nums[hi] always 
                if  nums[mid] > nums[hi]:
                    low = mid + 1
                
                elif nums[mid] < nums[hi]:
                    hi = mid
    def search(self, nums, target):

        ln = len(nums)
        minimum = float('inf')
        
        pivot = self.getPivot(nums)
        
        low = pivot
        hi  = pivot + ln - 1
        while low <= hi:
            mid = (low + hi)//2 
            middle = mid%ln
            if nums[middle] == target:
                return middle
            elif nums[middle] > target:
                hi = mid - 1
            else:
                low = mid + 1          
        return -1
         


```


```


class Solution:
    def search(self, A: List[int], B: int) -> int:
        low  = 0;
        high = len(A)-1;
        
        while low <= high :
            
            mid = low + (high-low)//2;
            
            if A[mid] == B:
                return mid;
                
            if A[low] <= A[mid]:
                
                if A[low] <= B and B <= A[mid]:
                    high = mid - 1;
                else:
                    low  = mid + 1; 
            else:
                if A[mid] <= B and B <= A[high]:
                    low = mid + 1;
                else:
                    high = mid - 1
        return -1


```
