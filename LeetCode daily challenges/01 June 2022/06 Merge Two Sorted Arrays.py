# https://leetcode.com/problems/merge-sorted-array/
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        
        k = (m+n-1)
        i, j = (m-1), (n-1)
        
        while i >= 0 and j >= 0:
            
            if nums2[j] >= nums1[i]:
                nums1[k] = nums2[j]
                j = j - 1
            
            else:
                nums1[k] = nums1[i]
                i = i - 1
            
            k = k - 1
        
        if j >= 0:
            nums1[0:k+1] = nums2[0:j+1]
            j = j - 1
        else:
            nums1[0:]