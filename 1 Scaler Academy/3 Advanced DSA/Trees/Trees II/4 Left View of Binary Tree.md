### PRint Left View of Binary Tree

https://practice.geeksforgeeks.org/problems/left-view-of-binary-tree/1

```

from collections import deque;

class Solution:

    def solve(self, root):

        if not root:
            return;
        q = deque([root]);
    
        return self.leftView(q);
    
    def leftView(self,q):

        leftView_list = [];

        while q:

            for i in range(len(q)):
                node = q.popleft();
                if i == 0:
                    leftView_list.append(node.val);
                if node.left:
                    q.append(node.left);
                if node.right:
                    q.append(node.right);
        
        return leftView_list;
    
```




