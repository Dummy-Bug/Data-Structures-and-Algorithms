### Problem Description

Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
Return k.
Custom Judge:

The judge will test your solution with the following code:

int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}
If all assertions pass, then your solution will be accepted.

 

Example 1:

Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
Example 2:

Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
 

Constraints:

1 <= nums.length <= 3 * 104
-100 <= nums[i] <= 100
nums is sorted in non-decreasing order.


Algorithm
By analyzing the above three key observations, we can derive the following algorithm,

Start both indexes (insertIndex, i) from 1.
insertIndex and i represents our First and second Index respectively.

Check if the previous element is different from the current element
The previous element is the element just before our i index i.e element present at arr[i-1]

If found different then perform arr[insertIndex] = arr[i] and increment insertIndex by 1

Increment i index by 1 till we reach end of the array

Note: After reaching the end of the array, our insertIndex variable will hold the count of unique elements in our input array.



```

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        size = len(nums)
        insertIndex = 1
        for i in range(1, size):
            # Found unique element
            if nums[i - 1] != nums[i]:      
                # Updating insertIndex in our main array
                nums[insertIndex] = nums[i] 
                # Incrementing insertIndex count by 1 
                insertIndex = insertIndex + 1       
        return insertIndex
        
```


```

class Solution:

    def removeDuplicates(self, A):
        
        i = 0; shift = 0;
        
        while i < len(A):
            
            A[i-shift] = A[i];
            
            i += 1;
            
            while i<len(A) and A[i] == A[i-1]:
                shift += 1;
                i += 1;
                        
        return len(A)-shift;

```
