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
    
```




