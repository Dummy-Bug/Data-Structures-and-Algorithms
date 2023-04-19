### Problem Description 

Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

 

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
 

Constraints:

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106


```

class Solution:
    def findMedianSortedArrays(self,nums1, nums2):
      
        
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2,nums1)
            
        
        low, high = 0, len(nums1) # Have to take whole length 
        desired   = (len(nums1)+len(nums2)+1)//2
        
        while low <= high :
            
            count1 = (low+high)>>1 # give us number of elements to take from first Array
            
            count2 = (desired-count1)
            # print(count1,count2)
            left1 = nums1[count1-1] if count1 != 0 else float('-inf')
            left2 = nums2[count2-1] if count2 != 0 else float('-inf')
            
            right1 = nums1[count1] if count1 != len(nums1) else float('inf')
            right2 = nums2[count2] if count2 != len(nums2) else float('inf')
            
            # print(left1,right2,left2,right1)
            if left1 <= right2 and left2 <= right1:
                
                if ( len(nums1)+len(nums2) ) %2 == 0: 
                    return ( max(left1,left2) + min(right1,right2) )/2.0
                else:
                    return max(left1,left2)
            
            elif left1 > right2:
                high = count1 - 1
            
            elif left2 > right1:
                low = count1 + 1
```
