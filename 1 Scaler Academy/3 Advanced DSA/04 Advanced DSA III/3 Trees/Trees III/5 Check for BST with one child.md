### Problem Description

Given preorder traversal of a binary tree, check if it is possible that it is also a preorder traversal of a Binary Search Tree (BST), where each internal node (non-leaf nodes) have exactly one child.



Problem Constraints

1 <= number of nodes <= 100000



Input Format

First and only argument is an integer array denoting the preorder traversal of binary tree.



Output Format

Return a string "YES" if true else "NO".



Example Input

Input 1:

 A : [4, 10, 5, 8]
Input 2:

 A : [1, 5, 6, 4]


Example Output

Output 1:

 "YES"
Output 2:

 "NO"


Example Explanation

Explanation 1:

 The possible BST is:
            4
             \
             10
             /
             5
              \
              8
Explanation 2:

 There is no possible BST which have the above preorder traversal.


**Solution Approach**

-> In Preorder traversal, descendants (or Preorder successors) of every node appear after the node.

We can say, if all internal nodes have only one child in a BST, then all the descendants of every node are either smaller or larger than the node.

To check the above condition:

Scan the last two nodes of preorder & mark them as min & max.

Scan every node down the preorder array. Each node must be either smaller than the min node or larger than the max node. Update min & max accordingly.


```

class Solution:

    def solve(self, A):

        minimum,maximum = float('-inf'),float('inf');

        for i in range(1,len(A)):

            curr_val = A[i];

            if curr_val>A[i-1] and curr_val<maximum:
                minimum = A[i-1];
                continue;
            elif curr_val<A[i-1] and curr_val>minimum:
                maximum = A[i-1];
                continue;
            return "NO";
        return "YES";


```
