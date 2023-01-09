### Problem Description

Given an integer array A, sort the array using QuickSort.



Problem Constraints

1 <= |A| <= 105

1 <= A[i] <= 109



Input Format

First argument is an integer array A.



Output Format

Return the sorted array.



Example Input

Input 1:

 A = [1, 4, 10, 2, 1, 5]
Input 2:

 A = [3, 7, 1]


Example Output

Output 1:

 [1, 1, 2, 4, 5, 10]
Output 2:

 [1, 3, 7]


Example Explanation

Explanation 1:

 Return the sorted array.
 
 
 **Approach**
 
There are many sorting algorithms, but for this problem we will use QuickSort of sort the array.
QuickSort is a Divide and Conquer Algorithm. It picks an element as pivot and partitions the given array around the picked pivot.

There are many different versions of quickSort that pick pivot in different ways:

-> Always pick first element as pivot.
-> Always pick last element as pivot (implemented below)
-> Pick a random element as pivot.
-> Pick median as pivot.

The key process in quickSort is partition().
Target of partitions is, given an array and an element x of array as pivot, put x at its correct position in sorted array and put all 
smaller elements (smaller than x) before x, and put all greater elements (greater than x) after x.
All this should be done in linear time.

Average Case Time Complexity : O(NlogN)
Worst Case : O(N2)
 
 ```
 
 class Solution:

    def solve(self, A):

        self.quick_sort(A,0,len(A)-1);

        return A;
    
    def quick_sort(self,nums,left,right):

        if left < right:

            partition_index = self.rearrange(nums,left,right);

            self.quick_sort(nums,left,partition_index-1);
            self.quick_sort(nums,partition_index+1,right);

    def rearrange(self,nums,start_index,end_index):

        left  = start_index + 1;
        right = end_index;

        while left <= right:

            if nums[left] <= nums[start_index]:
                left += 1;
            
            elif nums[right] > nums[start_index]:
                right -= 1;
            
            else:
                nums[left],nums[right] = nums[right], nums[left];
        
        nums[start_index],nums[left-1] = nums[left-1], nums[start_index]
        
        return left-1

 
 ```
