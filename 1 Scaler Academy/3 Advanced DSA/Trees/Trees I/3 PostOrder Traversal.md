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


