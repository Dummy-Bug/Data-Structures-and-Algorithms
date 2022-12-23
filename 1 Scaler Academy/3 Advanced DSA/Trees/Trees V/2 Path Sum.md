### Problem Description

Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

Problem Constraints
1 <= number of nodes <= 105

-100000 <= B, value of nodes <= 100000



Input Format
First argument is a root node of the binary tree, A.

Second argument is an integer B denoting the sum.



Output Format
Return 1, if there exist root-to-leaf path such that adding up all the values along the path equals the given sum. Else, return 0.



Example Input
Input 1:

 Tree:    5
         / \
        4   8
       /   / \
      11  13  4
     /  \      \
    7    2      1

 B = 22
Input 2:

 Tree:    5
         / \
        4   8
       /   / \
     -11 -13  4

 B = -1


Example Output
Output 1:

 1
Output 2:

 0


Example Explanation
Explanation 1:

 There exist a root-to-leaf path 5 -> 4 -> 11 -> 2 which has sum 22. So, return 1.
Explanation 2:

 There is no path which has sum -1.

**Solution Approach**

Recursion might make this problem much easier to solve.
You just need to keep a track of the sum from the root to the current node.
Then it becomes a question of just checking if the current node is a leaf node, and if so, do the sum match.

```

class Solution:

	def hasPathSum(self, root, target):
        if not root:
            return 0;
        if not root.left and not root.right and target==root.val:
            return 1;
        if self.hasPathSum(root.left,target-root.val) or self.hasPathSum(root.right,target-root.val):
            return 1;
        return 0;

```
