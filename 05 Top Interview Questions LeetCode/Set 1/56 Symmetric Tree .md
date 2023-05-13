### Problem Description 

Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

 

Example 1:


Input: root = [1,2,2,3,4,4,3]
Output: true
Example 2:


Input: root = [1,2,2,null,3,null,3]
Output: false
 

Constraints:

The number of nodes in the tree is in the range [1, 1000].
-100 <= Node.val <= 100
 

Follow up: Could you solve it both recursively and iteratively?


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
		
		if A == None:
			return 1;
		
		return self.isSameTree(A.left,A.right);
		

```
