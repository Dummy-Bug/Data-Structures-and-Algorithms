### Problem Description 

Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.
 

Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

```

class Solution:
    def __init__(self):
        self.freq_map = dict();
        
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        self.k = k-1;
        for i in range(len(nums)):
            if nums[i] not in self.freq_map:
                self.freq_map[nums[i]] = 0;
            self.freq_map[nums[i]] += 1;
        result = list(self.freq_map.keys());
        print(result)
            
        return self.helper(result,0,len(result)-1);
    
    def helper(self,result,start,end):
        while start<=end:
            pivot = random.randint(start,end);
            
            pivot_index = self.partition(result,start,end,pivot);
            
            if pivot_index == self.k:
                return result[:pivot_index+1];
            elif pivot_index > self.k:
                end = pivot_index-1;
            else:
                start = pivot_index+1;
    
    def partition(self,result,start,end,pivot):
        
        result[start],result[pivot] = result[pivot],result[start];
        
        pivot = start; right = end;
        left  = start+1;
        
        while left <= right:
            
            if self.freq_map[result[left]] > self.freq_map[result[pivot]]:
                left += 1;
            elif self.freq_map[result[right]] <= self.freq_map[result[pivot]]:
                right -= 1;
            else:
                result[left],result[right] = result[right],result[left];
                left += 1; right -= 1;
        
        result[left-1],result[pivot] = result[pivot],result[left-1];
        
        return left-1;

                
        
```
