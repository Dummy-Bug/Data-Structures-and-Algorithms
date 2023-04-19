### Probem Description 

Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 2000].
-100 <= Node.val <= 100


```
from collections import deque
dq = deque()
dq.append(root)

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
                return self.bfs(root)
        
    def bfs(self,root):        
        result = []
        level  = 0
        
        while dq :
            
            lst = []
            
            if level%2 == 0:
                
                for _ in range(len(dq)):
                    node = dq.popleft()
                    if node:
                        lst.append(node.val)
                        dq.append(node.left)
                        dq.append(node.right)
            else:
                for _ in range(len(dq)):
                    node = dq.pop()
                    if node:
                        lst.append(node.val)
                        dq.insert(0,node.right)
                        dq.insert(0,node.left)

            if lst != []:
                result.append(lst)
            level = level + 1
        
        return result
        
```
