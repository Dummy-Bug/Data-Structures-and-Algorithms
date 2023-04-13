https://leetcode.com/problems/binary-tree-inorder-traversal/

### Problem Description

Given the root of a binary tree, return the inorder traversal of its nodes' values.

Example 1:


Input: root = [1,null,2,3]
Output: [1,3,2]
Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [1]
Output: [1]
 

Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
 

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
