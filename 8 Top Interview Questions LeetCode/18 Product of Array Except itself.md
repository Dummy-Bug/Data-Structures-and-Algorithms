### Problem Description 

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 

Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
 
 **Two Pass Solution**
 
 ```
 
 class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)        
        for i in range(1, len(nums)):
            result[i] = nums[i-1] * result[i-1]
            
        right_prod = 1
        for i in range(len(nums)-1, -1, -1):
            result[i] *= right_prod
            right_prod *= nums[i]             
        
        return result
 
 ```
 
 -> The above process can be done in single pass as well. We were first calculating prefix product in one loop and then multiplying it with suffix product in another loop. These two process are independent of each other and can be done in the same loop. We just need to keep another prefix product variable similar to suffix_prod in previous approach.

We iterate from start and keep calculating prefix product & update corresponding ans[i] & at the same time we can calculate keep calculating suffix product from the end & update ans[n-1-i]


```

class Solution:
    def productExceptSelf(self, nums):
        ans, suf, pre ,n = [1]*len(nums), 1, 1,len(nums);

        for i in range(len(nums)):
            ans[i] = ans[i]*pre;# prefix product from one end
            ans[n-1-i] = ans[n-1-i]*suf;# suffix product from other end
            pre = pre*nums[i];
            suf = suf*nums[n-1-i];
        return ans

```
