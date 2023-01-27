### PreOrder traversal using Stack

https://www.interviewbit.com/problems/preorder-traversal/


**Solution Approach**

Think about using Stack.

Recursive call would look something like this :

print(root->val);
preorderprint(root->left);
preorderprint(root->right);

Instead of calling the functions, can you put the nodes on a stack and process them?

**Notes**

-> We can take the visited array and solve pre,post and in Order traversla problem

-> We can also modify the original input and solve these problems but we have to

-> solve these problems without above methods

```

from collections import deque;

class Solution:

	def preorderTraversal(self, A):

		if not A:
			return ;

		stack = deque([A]);
		preOrder = [];

		while stack:
			node = stack.pop();

			preOrder.append(node.val);

			if node.right:
				stack.append(node.right);
			if node.left:
				stack.append(node.left);
		return preOrder;

```		


**Best One**

```

from collections import deque;

class Solution:

	def preorderTraversal(self, A):

        stack = deque([]);
        curr  = A; preorderList = [];
    
        while stack or curr:

            while curr:
                preorderList.append(curr.val);
                stack.append(curr);
                curr = curr.left;

            curr = stack.pop();
            curr = curr.right;
            
        return preorderList;


```


