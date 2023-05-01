
### Largest BST SubTree

You are given a Binary Tree A with N nodes.

Write a function that returns the size of the largest subtree, which is also a Binary Search Tree (BST).

If the complete Binary Tree is BST, then return the size of the whole tree.

NOTE:

The largest subtree is the subtree with the most number of nodes.


Problem Constraints
1 <= N <= 105



Input Format
First and only argument is an pointer to root of the binary tree A.



Output Format
Return an single integer denoting the size of the largest subtree which is also a BST.



Example Input
Input 1:

     10
    / \
   5  15
  / \   \ 
 1   8   7
Input 2:

     5
    / \
   3   8
  / \ / \
 1  4 7  9


Example Output
Output 1:

 3
Output 2:

 7


Example Explanation
Explanation 1:

 Largest BST subtree is
                            5
                           / \
                          1   8
Explanation 2:

 Given binary tree itself is BST.

**Solution Approach**

  Maintain a data structure that stores for every node the maximum value in the subtree of a node, the minimum value in the subtree of a node,
  size of the subtree, size of the largest BST found in the subtree of a node, and flag to denote whether this subtree is bst or not.

  Traverse the tree in a bottom-up manner.

  A Tree is BST if the following is true for every node X.

  The largest value in the left subtree (of X) is smaller than the value of X.
  The smallest value in the right subtree (of X) is greater than the value of X.
  update the details of these nodes accordingly.

```

class Info:
    def __init__(self, size, max_val, min_val, ans, isBST):
        self.size    = size;
        self.max_val = int(max_val)
        self.min_val = int(min_val)
        self.ans     = ans
        self.isBST   = isBST

class Solution:

    def solve(self, A):

        res = self.largestBSTinBinaryTree(A)
        return res.ans

    def largestBSTinBinaryTree(self, root):

        if root == None:
            return Info(0, -2e9, 2e9, 0, True)
        if root.left == None and root.right == None:
            return Info(1, root.val, root.val, 1, True)

        l = self.largestBSTinBinaryTree(root.left)
        r = self.largestBSTinBinaryTree(root.right)

        ret = Info(0, 0, 0, 0, True);
        ret.size = 1 + l.size + r.size

        if l.isBST and r.isBST and l.max_val < root.val and r.min_val > root.val:
            ret.min_val = l.min_val
            ret.max_val = r.max_val
            ret.ans     = ret.size
            ret.isBST   = True
            return ret

        ret.ans = max(l.ans, r.ans)
        ret.isBST = False
        return ret;



```
