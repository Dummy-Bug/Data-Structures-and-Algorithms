### Problem Description 

Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.

Since the result may be very large, so you need to return a string instead of an integer.

 

Example 1:

Input: nums = [10,2]
Output: "210"
Example 2:

Input: nums = [3,30,34,5,9]
Output: "9534330"
 

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 109

```

class Solution:
    
    def compare(self,s1,s2):
        if s1+s2 < s2+s1:
            return 1;
        
        if s1+s2 == s2+s1:
            return 0;
        
        else:
            return -1

    def largestNumber(self, A):
        from functools import cmp_to_key;
        
        string_array = [];
        for i in range(len(A)):
            string_array.append(str(A[i]));
        
        # print(string_array)
        string_array.sort(key = cmp_to_key(self.compare));
        
        ans =  "".join(string_array);
        if ans[0] == '0':
            return '0'
        else:
            return ans

```
