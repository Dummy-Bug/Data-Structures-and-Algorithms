### Inorder Traversal using Stack

https://www.interviewbit.com/problems/inorder-traversal/

**Solution Approach**

> Think stack.

Recursive call would look something like this :

inorderprint(root->left);
print(root->val);
inorderprint(root->right);

Instead of calling the functions, can you put the nodes on a stack and process them?

How would your solution work if you could change the original tree?
How would it work if you were not allowed to change the tree but use additional memory ( track the number of times a node has appeared in the tree )?
How would it work if you were not even allowed the extra memory?


**Using Two Stacks**

```

from collections import deque;

class Solution:

	def inorderTraversal(self, A):
        if not A:
            return [];

        stack_A = deque([A]);
        stack_B = deque([]);
        inOrder = [];

        while stack_A:
            node = stack_A.pop();
            if node:
                stack_A.append(node.right);
                stack_A.append(node.left);
                stack_B.append(node);
            else:
                if stack_B:
                    node = stack_B.pop();
                    inOrder.append(node.val);

        return inOrder;

```

**Using Single Stack**

```

from collections import deque;

class Solution:

	def inorderTraversal(self, A):
        if not A:
            return [];

        stack = deque([A]);
        stack_B = deque([]);
        inOrder = [];

        while stack:
            node = stack.pop();
            if node:
                stack.append(node);
                stack.append(node.left);
            else:
                if stack:
                    node = stack.pop();
                    inOrder.append(node.val);
                    stack.append(node.right);

        return inOrder;

```

**Using node and stack**

```
    
    def inorderTraversal(self, A):
        self.stack = []
        self.result = []
        node = A
        while(self.stack or node):
            if node:
                self.stack.append(node)
                node = node.left
            else:
                node = self.stack.pop()
                self.result.append(node.val)
                node = node.right
        #print(self.result)
        return self.result
  
  ```      


  **Best One**
  
  ```
  
  from collections import deque;

class Solution:

	def inorderTraversal(self, A):

        stack = deque([]);
        curr  = A; inorderList = [];
    
        while stack or curr:

            while curr:

                stack.append(curr);
                curr = curr.left;
            
            curr = stack.pop();
            inorderList.append(curr.val);
            curr = curr.right;
        return inorderList;


    
  
  ```

