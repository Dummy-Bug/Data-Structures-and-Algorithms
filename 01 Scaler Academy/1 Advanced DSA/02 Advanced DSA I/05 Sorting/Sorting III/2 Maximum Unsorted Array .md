### Problem Description

Given an array A of non-negative integers of size N. Find the minimum sub-array Al, Al+1 ,..., Ar such that if we sort(in ascending order) 
that sub-array, then the whole array should get sorted. If A is already sorted, output -1.



Problem Constraints
1 <= N <= 1000000
1 <= A[i] <= 1000000



Input Format
First and only argument is an array of non-negative integers of size N.



Output Format
Return an array of length two where the first element denotes the starting index(0-based) and the second element denotes the ending index(0-based)
of the sub-array. If the array is already sorted, return an array containing only one element i.e. -1.



Example Input
Input 1:

A = [1, 3, 2, 4, 5]
Input 2:

A = [1, 2, 3, 4, 5]


Example Output
Output 1:

[1, 2]
Output 2:

[-1]


Example Explanation
Explanation 1:

If we sort the sub-array A1, A2, then the whole array A gets sorted.
Explanation 2:

A is already sorted.

**Sorting**

```

class Solution:
    def findUnsortedSubarray(self, A: List[int]) -> int:
        # Sorting
        sorted_arr = sorted(A);
        
        i = 0; j = len(A)-1;
        start_index = float('inf');
        end_index   = float('-inf');
        
        for i in range(len(A)):
            
            if A[i] != sorted_arr[i]:
                start_index = min(start_index,i);
                end_index   = max(end_index,i);
        
        if start_index == float('inf') or end_index == float('inf'):
            return 0;
        
        return end_index-start_index+1
        

```

**Stack**

Algorithm

The idea behind this approach is also based on selective sorting. We need to determine the correct position of the minimum and 
the maximum element in the unsorted subarray to determine the boundaries of the required unsorted subarray.

To do so, in this implementation, we make use of a stackstack. We traverse over the numsnums array starting from the beginning.
As we go on facing elements in ascending order(a rising slope), we keep on pushing the elements' indices over the stackstack. 
This is done because such elements are in the correct sorted order(as it seems till now). As soon as we encounter a falling 
slope, i.e. an element nums[j]nums[j] which is smaller than the element on the top of the stackstack, we know that nums[j]nums[j] 
isn't at its correct position.

In order to determine the correct position of nums[j]nums[j], we keep on popping the elemnents from the top of the stackstack until we 
reach the stage where the element(corresponding to the index) on the top of the stackstack is lesser than nums[j]nums[j]. Let's say the 
popping stops when the index on stackstack's top is kk. Now, nums[j]nums[j] has found its correct position. It needs to lie at an index 
k + 1k+1.

We follow the same process while traversing over the whole array, and determine the value of minimum such kk. This marks the left boundary
of the unsorted subarray.

Similarly, to find the right boundary of the unsorted subarray, we traverse over the numsnums array backwards. This time we keep on 
pushing the elements if we see a falling slope. As soon as we find a rising slope, we trace forwards now and determine the larger 
element's correct position. We do so for the complete array and thus, determine the right boundary.

We can look at the figure below for reference. We can observe that the slopes directly indicate the relative ordering. We can also 
observe that the point bb needs to lie just after index 0 marking the left boundary and the point aa needs to lie just before index 
7 marking the right boundary of the unsorted subarray.

```

public class Solution {
    public int findUnsortedSubarray(int[] nums) {
        Stack < Integer > stack = new Stack < Integer > ();
        int l = nums.length, r = 0;
        for (int i = 0; i < nums.length; i++) {
            while (!stack.isEmpty() && nums[stack.peek()] > nums[i])
                l = Math.min(l, stack.pop());
            stack.push(i);
        }
        stack.clear();
        for (int i = nums.length - 1; i >= 0; i--) {
            while (!stack.isEmpty() && nums[stack.peek()] < nums[i])
                r = Math.max(r, stack.pop());
            stack.push(i);
        }
        return r - l > 0 ? r - l + 1 : 0;
    }
}

```

**Without Extra Space**

Algorithm

The idea behind this method is that the correct position of the minimum element in the unsorted subarray helps to determine the required 
left boundary. Similarly, the correct position of the maximum element in the unsorted subarray helps to determine the required right boundary.

Thus, firstly we need to determine when the correctly sorted array goes wrong. We keep a track of this by observing rising slope starting 
from the beginning of the array. Whenever the slope falls, we know that the unsorted array has surely started. Thus, now we determine the 
minimum element found till the end of the array numsnums, given by minmin.

Similarly, we scan the array numsnums in the reverse order and when the slope becomes rising instead of falling, we start looking for the 
maximum element till we reach the beginning of the array, given by maxmax.

Then, we traverse over numsnums and determine the correct position of minmin and maxmax by comparing these elements with the other array elements.
e.g. To determine the correct position of minmin, we know the initial portion of numsnums is already sorted. Thus, we need to find the first 
element which is just larger than minmin. Similarly, for maxmax's position, we need to find the first element which is just smaller than maxmax 
searching in numsnums backwards.

```

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        
        min_num   = float('inf');
        max_num   = float('-inf');
        flag = False;
        
        for i in range(1,len(nums)):
            if nums[i] < nums[i-1]:
                flag = True;
            
            if flag == True:
                min_num = min(min_num,nums[i]);
        if not flag:
            return 0;
        flag = False;
        
        for i in range(len(nums)-2,-1,-1):
            if nums[i] > nums[i+1]:
                flag = True;
            if flag:
                max_num = max(max_num,nums[i]);
        print(min_num,max_num);
        for i in range(len(nums)):
            if nums[i]>min_num:
                left = i;
                break;
        for i in range(len(nums)-1,-1,-1):
            if nums[i]<max_num:
                right = i;
                break;
        return right-left+1

```

