### Right view of Binary Tree


https://www.interviewbit.com/problems/right-view-of-binary-tree/

```

from collections import deque;

class Solution:

    def solve(self, A):

        q = deque([A]);
        return self.rightView(q);

    def rightView(self,q):

            rightView_list = [];

            while q:
                curr_len = len(q);
                for i in range(curr_len):
                    node = q.popleft();
                    if i == curr_len-1:
                        rightView_list.append(node.val);
                    if node.left:
                        q.append(node.left);
                    if node.right:
                        q.append(node.right);
            
            return rightView_list;


```
