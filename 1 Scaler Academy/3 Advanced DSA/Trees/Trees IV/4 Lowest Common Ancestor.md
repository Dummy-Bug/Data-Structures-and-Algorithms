### Problem Description

Find the lowest common ancestor in an unordered binary tree A, given two values, B and C, in the tree.
Lowest common ancestor: the lowest common ancestor (LCA) of two nodes and w in a tree or directed acyclic graph (DAG) is the lowest 
(i.e., deepest) node that has both v and w as descendants.



Problem Constraints
1 <= size of tree <= 100000

1 <= B, C <= 109



Input Format
First argument is head of tree A.

Second argument is integer B.

Third argument is integer C.



Output Format
Return the LCA.



Example Input
Input 1:

 
      1
     /  \
    2    3
B = 2
C = 3
Input 2:

      1
     /  \
    2    3
   / \
  4   5
B = 4
C = 5


Example Output
Output 1:

 1
Output 2:

 2


Example Explanation
Explanation 1:

 LCA is 1.
Explanation 2:

 LCA is 2.


**Solution Approach**

Linear solution using path calculation :

1) Find a path from the root to n1 and store it in a vector or array.
2) Find a path from the root to n2 and store it in another vector or array.
3) Traverse both paths till the values in arrays are the same. Return the common element just before the mismatch

Linear solution using recursion :

We traverse from the bottom, and once we reach a node that matches one of the two nodes, we pass it up to its parent. 
The parent will then test its left and right subtree if each contains one of the two nodes. If yes, then the parent must be the LCA, and 
we pass its parent up to the root. If not, we pass the lower node, which contains either one of the two nodes 
(if the left or right subtree contains either p or q) or NULL (if both the left and right subtree does not contain either p or q) up.


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
