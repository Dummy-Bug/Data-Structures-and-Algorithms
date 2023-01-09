### Problem Description

Find the Bth smallest element in given array A .

NOTE: Users should try to solve it in less than equal to B swaps.



Problem Constraints
1 <= |A| <= 100000

1 <= B <= min(|A|, 500)

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


**Approach**

The algorithm of selection sort should be used.
The selection sort algorithm sorts an array by repeatedly
finding the minimum element (considering ascending order)
from unsorted part and putting it at the beginning.
You need to get the minimum element to the beginning of the array
only B times as you require the Bth element.

```

class Solution:

	def kthsmallest(self, A, k):

        A = list(A);
        for i in range(k):

            mini  = A[i];
            index = i;

            for j in range(i+1,len(A)):

                if A[j] < mini:
                    mini = A[j];
                    index = j;
            
            temp = A[i];
            A[i] = A[index];
            A[index] = temp;

        return A[k-1];

```
