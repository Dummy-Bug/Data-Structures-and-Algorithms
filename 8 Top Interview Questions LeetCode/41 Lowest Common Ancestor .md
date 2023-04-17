### Problem Description 

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

 

Example 1:


Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.
Example 2:


Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
Example 3:

Input: root = [1,2], p = 1, q = 2
Output: 1
 

Constraints:

The number of nodes in the tree is in the range [2, 105].
-109 <= Node.val <= 109
All Node.val are unique.
p != q
p and q will exist in the tree.

```



class Solution:

    def lca(self, root, val1, val2):
        s1 = [];s2 = [];

        if self.path(root, s1, val1) == False or self.path(root, s2, val2) == False:
            return -1
        i = 0
        while i < len(s1) and i < len(s2):
            if s1[i] != s2[i]:
                break
            i += 1
        return s1[i - 1]

    def path(self, root, s, val):
        if root == None:
            return False
        s.append(root.val)
        if root.val == val:
            return True
        if ((self.path(root.left, s, val)) or (self.path(root.right, s, val))):
            return True
        s.pop()
        return False


```
