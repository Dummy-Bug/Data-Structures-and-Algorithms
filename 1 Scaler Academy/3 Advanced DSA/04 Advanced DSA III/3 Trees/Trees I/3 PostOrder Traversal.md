### PostOrder Traversal iterativiley

```

from collections import deque;

class Solution:

	def postorderTraversal(self, A):

        stack   = deque([]);
        prev_node = None;
        curr    = A; postorderList = [];

        while stack or curr:

            while curr:
                stack.append(curr);
                curr = curr.left;

            curr = stack.pop();

            if prev_node != curr.right:
                stack.append(curr);
                prev_node = curr;
                curr = curr.right;
            else:
                postorderList.append(curr.val);
                curr = None; # so that we can ignore the while loop 
                             # and directly start traversing right child.
        
        return postorderList;

```

**Best One Just like PreOrder**


```

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def postorderTraversal(self, A):
        res = []
        stack = [A]
        while stack:
            pop = stack.pop()
            res.append(pop.val)
            if pop.left:
                stack.append(pop.left)
            if pop.right:
                stack.append(pop.right)
        
        return res[::-1]

```
