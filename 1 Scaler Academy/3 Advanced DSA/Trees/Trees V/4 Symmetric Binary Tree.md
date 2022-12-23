### Problem Description

Given a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).



Problem Constraints
1 <= number of nodes <= 105



Input Format
First and only argument is the root node of the binary tree.



Output Format
Return 0 / 1 ( 0 for false, 1 for true ).



Example Input
Input 1:

    1
   / \
  2   2
 / \ / \
3  4 4  3
Input 2:

    1
   / \
  2   2
   \   \
   3    3


Example Output
Output 1:

 1
Output 2:

 0


Example Explanation
Explanation 1:

 The above binary tree is symmetric. 
Explanation 2:

The above binary tree is not symmetric.

**Solution Approach**

2 trees, T1 and T2, are symmetric if
1) value of T1’s root is the same as T2’s root
2) T1’s left and T2’s right are symmetric.
3) T2’s left and T1’s right are symmetric.

Can you use the above fact to model an easy recursion-based solution?

```

class Solution:
	def isSameTree(self, node1, node2):
		
		if node1 == None and node2 == None:
			return 1;
		
		if node1 == None or node2 == None:
			return 0;
		
		if node1.val != node2.val:
			return 0;
		
		return self.isSameTree(node1.left,node2.right) & self.isSameTree(node1.right,node2.left);
	
	def isSymmetric(self, A):
		
		return self.isSameTree(A.left,A.right);

```
