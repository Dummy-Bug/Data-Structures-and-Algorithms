### Level Order Traversal


```

from collections import deque;

class Solution:

    def bfs(self,node):
        ans = [];
        q = deque();
        q.append(node);
        
        while q:
            level_nodes = [];
            
            for _ in range(len(q)):
                
                node = q.popleft();
                level_nodes.append(node.val);
                
                if node.left:
                    q.append(node.left);
                if node.right:
                    q.append(node.right);
            ans.append(level_nodes);
        
        return ans;
                
   
	def levelOrder(self, A):

        return self.bfs(A);

```
