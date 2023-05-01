### Problem Description

Given an array with N objects colored red, white, or blue, sort them so that objects of the same color are adjacent, with the colors in the 
order red, white, and blue.

We will use the integers 0, 1, and 2 to represent red, white, and blue, respectively.

Note: Using the library sort function is not allowed.



Problem Constraints
1 <= N <= 1000000
0 <= A[i] <= 2


Input Format
First and only argument of input contains an integer array A.


Output Format
Return an integer array in asked order


Example Input
Input 1 :
    A = [0 1 2 0 1 2]
Input 2:

    A = [0]


Example Output
Output 1:
    [0 0 1 1 2 2]
Output 2:

    [0]


Example Explanation
Explanation 1:
    [0 0 1 1 2 2] is the required order.

There are multiple approaches possible here. We need to make sure we do not allocate extra memory.

**Approach 1:**

Count the number of red, white, and blue balls.
Then, in another pass, set the initial redCount number of cells as 0, next whiteCount cell as 1, and next blueCount cells as 2.
Requires two passes of the array.

**Approach 2:**

Swap the 0s to the start of the array maintaining a pointer, and 2s to the end of the array.
1s will automatically be in their right position.


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
