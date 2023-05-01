### DeSerialize the Binary Tree

Problem Description
You are given an integer array A denoting the Level Order Traversal of the Binary Tree.

You have to Deserialize the given Traversal in the Binary Tree and return the root of the Binary Tree.

NOTE:

In the array, the NULL/None child is denoted by -1.
For more clarification check the Example Input.


Problem Constraints
1 <= number of nodes <= 105

-1 <= A[i] <= 105



Input Format
Only argument is an integer array A denoting the Level Order Traversal of the Binary Tree.



Output Format
Return the root node of the Binary Tree.



Example Input
Input 1:

 A = [1, 2, 3, 4, 5, -1, -1, -1, -1, -1, -1]
Input 2:

 A = [1, 2, 3, 4, 5, -1, 6, -1, -1, -1, -1, -1, -1]


Example Output
Output 1:

           1
         /   \
        2     3
       / \
      4   5
Output 2:

            1
          /   \
         2     3
        / \ .   \
       4   5 .   6


Example Explanation
Explanation 1:

 Each element of the array denotes the value of the node. If the val is -1 then it is the NULL/None child.
 Since 3, 4 and 5 each has both NULL child we had represented that using -1.
Explanation 2:

 Each element of the array denotes the value of the node. If the val is -1 then it is the NULL/None child.
 Since 3 has left child as NULL while 4 and 5 each has both NULL child.

**Solution Approach**

 We can do this simply by using a queue data structure.

 We know that the root node will always be the first element of level order traversal.
 Create a root node and push the root node into the queue.

 Now, run a loop until the queue is empty and keep a variable, let’s say i, for denoting the current index in the Level Order Traversal.

 Pop the Node: If the node is not NULL, then the element at index i will be the left child, and the element at i+1 will be the right child.
 Create those children and push the left child and right child of the node, respectively, in the queue.

 After building the tree, return the root node

```

import sys 
  
# the setrecursionlimit function is used to modify the default recursion limit set by python. Using this, we can increase the recursion limit to satisfy our needs 
  
sys.setrecursionlimit(10**6) 

from collections import deque 

class Solution:
    def solve(self, A):
        root = TreeNode(A[0])
        q = deque()
        q.append(root)
        i = 1
        while(len(q) != 0):
            cur = q.popleft()
            if(cur == None):
                continue
            val_left  = A[i]
            val_right = A[i+1]
            i += 2
            if(val_left == -1):
                cur.left = None
            else:
                cur.left = TreeNode(val_left)
            if(val_right == -1):
                cur.right = None
            else:
                cur.right = TreeNode(val_right)
            q.append(cur.left)
            q.append(cur.right)
        return root

```
