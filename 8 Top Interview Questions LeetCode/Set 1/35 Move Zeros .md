### Problem Description 

Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]
 

Constraints:

1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1


**Use Conecpt of Sort Colors**


```

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        nonZeroPtr = 0; # will move if points to nonZeroElements
        zeroPtr    = 0; # will move if points to Zero
        
        while nonZeroPtr < len(nums) and zeroPtr < len(nums):
            
            if zeroPtr < nonZeroPtr:
                zeroPtr = nonZeroPtr;
                
            elif nums[nonZeroPtr] != 0:
                nonZeroPtr += 1;
            
            elif nums[zeroPtr] == 0:
                zeroPtr += 1;
            
            else:
                nums[nonZeroPtr],nums[zeroPtr] = nums[zeroPtr],nums[nonZeroPtr];


```


**Shift Concepts of InterviewBit**


```


class Solution:
    def moveZeroes(self, A: List[int]) -> None:
        
        shift = 0;
        
        for i in range(len(A)):
            
            if A[i] == 0:
                shift += 1;
            else:
                A[i-shift],A[i] = A[i], A[i-shift];
        
        
```
