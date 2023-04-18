### Problem Description 

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

 

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
 

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109


```

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        st = set(nums)
        
        longest_seq = 0
        curr_seq    = 0
        
        for num in nums:
            
            if num-1 not in st: # if current element is not a part of any sequence 
                
                curr_num = num
                curr_seq = 1
                
                while curr_num+1 in st:
                    curr_seq += 1
                    curr_num += 1
                
                longest_seq = max(longest_seq,curr_seq)
        
        return longest_seq
                
        

```
