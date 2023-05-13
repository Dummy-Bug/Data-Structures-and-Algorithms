### Problem Description 

Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

 

Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Example 2:

Input: nums = [2,0,1]
Output: [0,1,2]
 

Constraints:

n == nums.length
1 <= n <= 300
nums[i] is either 0, 1, or 2.
 

Follow up: Could you come up with a one-pass algorithm using only constant extra space?


```


public class Solution {
    public void swap(int []array,int i,int j){
        int temp = array[i];
        array[i] = array[j];
        array[j] = temp;
    }
    public int[] sortColors(int[] A) {

        int p1 = 0;int  p2 = 0,p3 = A.length-1;

        while(p2<=p3){
            if (A[p2] == 1)p2++;
            else if (A[p2] == 0){swap(A,p2,p1); p1++;p2++;}
            else {swap(A,p3,p2); p3--;}
        }
        return A;
    }
}

```
