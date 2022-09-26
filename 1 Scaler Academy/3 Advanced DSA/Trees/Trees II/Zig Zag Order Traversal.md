### Compute the ZigZag order level traversal

https://www.interviewbit.com/problems/zigzag-level-order-traversal-bt/

```

from collections import deque;

class Solution:

	def zigzagLevelOrder(self, root):

        q = deque([root]); result = [];
        level = 0;

        while q:
            temp = [];
            for i in range(len(q)):
                node = q.popleft();

                temp.append(node.val);
                if node.left:
                    q.append(node.left);
                if node.right:
                    q.append(node.right);
            if level%2 == 0:
                result.append(temp)
            else:
                result.append(temp[::-1]);
            level += 1;
        return result;

```
