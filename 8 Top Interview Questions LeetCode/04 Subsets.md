https://leetcode.com/problems/subsets/description/

### Problem Description 

Given an integer array nums of unique elements, return all possible 
subsets(the power set).
The solution set must not contain duplicate subsets. Return the solution in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [0]
Output: [[],[0]]
 

Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10
All the numbers of nums are unique.


```

from collections import deque;
stack = deque([]);

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        global allSubsets;
        allSubsets = [];

        self.helper(nums,0,stack);
        return allSubsets;
    
    def helper(self,nums,startIndex,stack):
        
        allSubsets.append(list(stack));
        
        for i in range(startIndex,len(nums)):
            stack.append(nums[i]);
            self.helper(nums,i+1,stack);
            stack.pop();
            

```
