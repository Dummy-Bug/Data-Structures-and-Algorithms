https://leetcode.com/problems/maximum-depth-of-binary-tree/description/

### problem description

Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 3
Example 2:

Input: root = [1,null,2]
Output: 2
 

```

class Solution:
    def maxDepth(self, root: Optional[TreeNode]):
        
    # maximum depth is nothing but height of the tree.
    
        return self.height(root)
    
    def height(self,root):
        
        if not root:
            return 0
        
        left  = self.height(root.left)
        
        right = self.height(root.right)
        
        return (1 + max(left,right))

```
