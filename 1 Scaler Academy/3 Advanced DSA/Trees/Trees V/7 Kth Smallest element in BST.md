### Problem Description

Given a binary search tree represented by root A, write a function to find the Bth smallest element in the tree.

Problem Constraints
1 <= Number of nodes in binary tree <= 100000

0 <= node values <= 10^9



Input Format
First and only argument is head of the binary tree A.



Output Format
Return an integer, representing the Bth element.



Example Input
Input 1:

 
            2
          /   \
         1    3
B = 2
Input 2:

 
            3
           /
          2
         /
        1
B = 1



Example Output
Output 1:

 2
Output 2:

 1


Example Explanation
Explanation 1:

2nd element is 2.
Explanation 2:

1st element is 1.

```

class Solution:

	def kthsmallest(self, root, k):
        self.result = 0;
        self.count  = 0;
        self.helper(root,k,1);
        return self.result;
    
    def helper(self,node,k,count):

        if not node:
            return ;
        self.helper(node.left,k,count);
        self.count += 1;
        if self.count == k:
            self.result = node.val;
            return;
        self.helper(node.right,k,count);

```

**Solution Approach**

Note the property of the binary search tree.
All elements smaller than root will be in the left subtree, and all elements greater than root will be in the right subtree.
This means we need not even explore the right subtree till we have explored everything in the left subtree. Or in other words, we go to the right subtree only when the size of left subtree + 1 ( root ) < k.

With that in mind, we can come up with an easy recursive solution which is similar to inorder traversal :

Step 1: Find the kth smallest element in left subtree decrementing k for every node visited. If answer is found, return answer.
Step 2: Decrement k by 1. If k == 0 ( this node is the kth node visited ), return node’s value
Step 3: Find the kth smallest element in right subtree.


```

class Solution:

    def kthsmallest(self, A, B):

        stack = []
        cur   = A;
        while stack or cur:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                B -= 1
                if B == 0:
                    return cur.val
                cur = cur.right
        return None

```
