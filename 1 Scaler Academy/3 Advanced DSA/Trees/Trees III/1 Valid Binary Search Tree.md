### Check if Binary Tree is Valid Binary Search Tree

https://leetcode.com/problems/validate-binary-search-tree/


**Approach 1**

```

class Solution:

	def isValidBST(self, A):
		inorder_list = []
		self.Inorder(A,inorder_list);

		for i in range(1,len(inorder_list)):
			if inorder_list[i] <= inorder_list[i-1]:
				return 0;
		return 1;
	
	def Inorder(self,node,inorder_list):
		if not node:
			return;
		
		self.Inorder(node.left,inorder_list);
		inorder_list.append(node.val);
		self.Inorder(node.right,inorder_list);
		return;


```

**Notes**
-> There is better way of doing it without using the extra space of storing all the nodes

The trick is when we traverse down the tree, maintain max and min allowed values for the subtree, and check that the node’s value should lie between the allowed max and min. The initial values for min and max should be INT_MIN and INT_MAX.

If at the current node, allowed min is minn and allowed max is maxx.

If we move to the left, then the max value in the left subtree should be smaller than the node. So, update maxx = min(maxx, value of node).
Similarly, If we move to the right, the min value in the right subtree should be greater than the node.So, update minn = max(minn, value of node).

In this, we are traversing each node only once. So, the time complexity is O(n).


```
class Solution:

	def isValidBST(self, A):

		return self.ValidBst(A,-1,float('inf'));
	
	def ValidBst(self,node,left_max,right_max):

		if not node:
			return 1;
		if node.val < left_max or node.val > right_max:
			return 0;
		left  = self.ValidBst(node.left,left_max,node.val-1)
		right = self.ValidBst(node.right,node.val+1,right_max)
		
		return 0 if not (left and right ) else 1;
		

```
