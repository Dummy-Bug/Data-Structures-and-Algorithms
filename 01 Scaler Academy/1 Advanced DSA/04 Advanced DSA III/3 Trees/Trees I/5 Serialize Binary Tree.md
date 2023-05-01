### Serialize the Binary Tree

https://www.geeksforgeeks.org/serialize-deserialize-binary-tree/



```

from collections import deque;

class Solution:

    def solve(self, A):

        queue = deque([A]);
        serialized_tree = [];

        while queue:

            node = queue.popleft();

            if node:
                serialized_tree.append(node.val);
                queue.append(node.left);
                queue.append(node.right);
            else:
                serialized_tree.append(-1);
        
        return serialized_tree;

```



