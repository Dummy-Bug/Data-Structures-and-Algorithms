### Problem Description

Find the Bth smallest element in an unsorted array of non-negative integers A.
Definition of kth smallest element: The kth smallest element is the minimum possible n such that there are at least k elements in the array <= n.
In other words, if the array A was sorted, then Ak - 1

NOTE: You are not allowed to modify the array (The array is read-only). Try to do it using constant extra space.



Problem Constraints
1 <= |A| <= 106

1 <= B <= |A|

1 <= A[i] <= 109



Input Format
The first argument is an integer array A.

The second argument is integer B.



Output Format
Return the Bth smallest element in given array.



Example Input
Input 1:

A = [2, 1, 4, 3, 2]
B = 3
Input 2:

A = [1, 2]
B = 2


Example Output
Output 1:

 2
Output 2:

 2


Example Explanation
Explanation 1:

 3rd element after sorting is 2.
Explanation 2:

 2nd element after sorting is 2.


**Using Quick Sort**
--> Also called as Quick Select;

```

class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def kthsmallest(self, A, k):
        # print(A)
        nums = list(A);
        self.k = k-1;
        return self.helper(nums,0,len(nums)-1);
        
    
    def helper(self,nums,start,end):
        
        while start <= end:
            
            pivot_index = self.partition(nums,start,end);
            # print(pivot_index)
            if pivot_index == self.k:
                return nums[pivot_index];
            
            elif pivot_index > self.k:
                return self.helper(nums,start,pivot_index-1);
            else:
                return self.helper(nums,pivot_index+1,end);
    
    def partition(self,nums,start,end):
        
        pivot_index = start;
        left = start+1; right = end;
        # conditions for kth largest and kth smallest would be different   
        while left<=right:
            
            if nums[left] <= nums[pivot_index]:
                left += 1;
            
            elif nums[right] > nums[pivot_index]:
                right -= 1;
            else:
                nums[left],nums[right] = nums[right],nums[left];
                left  += 1;
                right -=1 
        
        nums[pivot_index],nums[left-1] = nums[left-1],nums[pivot_index];
        
        return left-1;
        


```
