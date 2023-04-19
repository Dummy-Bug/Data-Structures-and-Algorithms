https://leetcode.com/problems/majority-element/

### Problem Description 

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2

```

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        # Should try it with random.choic(nums) as well
       
    # """ Boyer-Moore Voting Algorithm """
    
        count = 0
        for num in nums:
            
            if count == 0: # Make the current number the candidate
                candidate = num
                count += 1
            
            else:
                if num == candidate: # if curr_num is our candidate ele then increase the count
                    count += 1
                else:
                    count -= 1
        
        return candidate 
    # This happens because if an element is present > n//2 times then it's count 
    # will always be > 0 as it will outscore every other element .
        
            
```
