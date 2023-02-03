### Problem Description 

Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is
greater than or equal to target. If there is no such subarray, return 0 instead.

 https://leetcode.com/problems/minimum-size-subarray-sum/

Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1
Example 3:

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
 

Constraints:

1 <= target <= 109
1 <= nums.length <= 105
1 <= nums[i] <= 104
 

Follow up: If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log(n)).
    

    
    
```


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]):
        i, j = 0, 0
        result = float("inf")
        curr_sum = 0
        
        while j < len(nums):
            curr_sum += nums[j]
            while curr_sum >= target:
                result = min(result,j-i+1)
                curr_sum = curr_sum - nums[i]
                i = i + 1
            j = j + 1
        if result == float("inf"):
            return 0
        return result
  


```
 
**Java Code**


```


class Solution {
    public int minSubArrayLen(int target, int[] nums) 
    {
        int result = nums.length+1;
        int i=0,j=0;
        long curr_sum = 0;
        
        while ( j<nums.length )
        {
            curr_sum += (long)nums[j];
            
            if ( curr_sum < target )
            {
                j += 1;continue;
            }
            
            while (curr_sum >= target )
            {
                result   = Math.min(result,j-i+1);
                curr_sum = curr_sum - (long)nums[i];
                i += 1;
            }
            j += 1;
            
        }
        if ( result == nums.length + 1 )
        {
            return 0;
        }
        return result;
    }
}


```
