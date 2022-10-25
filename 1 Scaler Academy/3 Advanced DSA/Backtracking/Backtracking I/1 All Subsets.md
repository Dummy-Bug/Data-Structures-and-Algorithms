### Problem Description

Given a set of distinct integers A, return all possible subsets.

NOTE:

Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.
Also, the subsets should be sorted in ascending ( lexicographic ) order.
The list is not necessarily sorted.


Problem Constraints
1 <= |A| <= 16
INTMIN <= A[i] <= INTMAX


Input Format
First and only argument of input contains a single integer array A.



Output Format
Return a vector of vectors denoting the answer.



Example Input
Input 1:

A = [1]
Input 2:

A = [1, 2, 3]


Example Output
Output 1:

[
    []
    [1]
]
Output 2:

[
 []
 [1]
 [1, 2]
 [1, 2, 3]
 [1, 3]
 [2]
 [2, 3]
 [3]
]


Example Explanation
Explanation 1:

 You can see that these are all possible subsets.
Explanation 2:

You can see that these are all possible subsets.



```

from collections import deque;
class Solution:

	def subsets(self, A):
		self.AllSubsets = [];

		self.backtrack(sorted(A),0,deque([]));
        return sorted(self.AllSubsets);
    
    def backtrack(self,arr,curr_index,curr_stack):

        if len(arr) <= curr_index:

            self.AllSubsets.append(list(curr_stack));
            return;
        
        self.backtrack(arr,curr_index+1,curr_stack);
        curr_stack.append(arr[curr_index]);
        self.backtrack(arr,curr_index+1,curr_stack);
        curr_stack.pop();
        

```
