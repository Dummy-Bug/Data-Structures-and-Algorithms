### Problem Description

Given a binary search tree.
Return the distance between two nodes with given two keys B and C. It may be assumed that both keys exist in BST.

NOTE: Distance between two nodes is number of edges between them.



Problem Constraints
1 <= Number of nodes in binary tree <= 1000000

0 <= node values <= 109



Input Format
First argument is a root node of the binary tree, A.

Second argument is an integer B.

Third argument is an integer C.



Output Format
Return an integer denoting the distance between two nodes with given two keys B and C



Example Input
Input 1:

    
         5
       /   \
      2     8
     / \   / \
    1   4 6   11
 B = 2
 C = 11
Input 2:

    
         6
       /   \
      2     9
     / \   / \
    1   4 7   10
 B = 2
 C = 6


Example Output
Output 1:

 3
Output 2:

 1


Example Explanation
Explanation 1:

 Path between 2 and 11 is: 2 -> 5 -> 8 -> 11. Distance will be 3.
Explanation 2:

 Path between 2 and 6 is: 2 -> 6. Distance will be 1


```

class Solution:
    def solve(self, root, val1, val2):
        s1 = [];s2 = [];

        if self.path(root, s1, val1) == False or self.path(root, s2, val2) == False:
            return -1
        i = 0
        while i < len(s1) and i < len(s2):
            if s1[i] != s2[i]:
                break
            i += 1
        return len(s1[i:])+len(s2[i:]);

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
  
  **Solution Approach**
  An efficient way to solve the above problem:

We start from the root and for every node, we do following.

If both keys are greater than the current node, we move to the right child of the current node.
If both keys are smaller than current node, we move to left child of current node.
If one keys is smaller and other key is greater, current node is Lowest Common Ancestor (LCA) of two nodes. We find distances of current node from two keys and return sum of the distances.

Time Complexity : O(h) (height of Tree)

```

def distanceFromRoot(root, x):
    if (root.val == x):
        return 0
    elif (root.val > x):
        return 1 + distanceFromRoot(root.left, x)
    return 1 + distanceFromRoot(root.right, x);

def distanceBetween2( root, a, b):
    if (root == None):
        return 0
    if (root.val > a and root.val > b):
        return distanceBetween2(root.left, a, b)
    if (root.val < a and root.val < b):
        return distanceBetween2(root.right, a, b)
    if (root.val >= a and root.val <= b):
        return distanceFromRoot(root, a) + distanceFromRoot(root, b)

class Solution:

    def solve(self, A, B, C):
        if (B > C):
            B, C = C, B
        return distanceBetween2(A, B, C)

```
