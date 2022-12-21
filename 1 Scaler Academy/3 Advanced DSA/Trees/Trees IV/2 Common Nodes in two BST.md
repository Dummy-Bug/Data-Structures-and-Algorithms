### Problem Description

Given two BST's A and B, return the (sum of all common nodes in both A and B) % (109 +7) .

In case there is no common node, return 0.

NOTE:

Try to do it one pass through the trees.



Problem Constraints
1 <= Number of nodes in the tree A and B <= 105

1 <= Node values <= 106



Input Format
First argument represents the root of BST A.

Second argument represents the root of BST B.



Output Format
Return an integer denoting the (sum of all common nodes in both BST's A and B) % (109 +7) .



Example Input
Input 1:

 Tree A:
    5
   / \
  2   8
   \   \
    3   15
        /
        9

 Tree B:
    7
   / \
  1  10
   \   \
    2  15
       /
      11
Input 2:

  Tree A:
    7
   / \
  1   10
   \   \
    2   15
        /
       11

 Tree B:
    7
   / \
  1  10
   \   \
    2  15
       /
      11


Example Output
Output 1:

 17
Output 2:

 46


Example Explanation
Explanation 1:

 Common Nodes are : 2, 15
 So answer is 2 + 15 = 17
Explanation 2:

 Common Nodes are : 7, 2, 1, 10, 15, 11
 So answer is 7 + 2 + 1 + 10 + 15 + 11 = 46
 
 
 **Solution Approach**
 
 Method 1 (Linear Time) We can find common elements in O(n) time.

1) Do inorder traversal of first tree and store the traversal in an auxiliary array ar1[].
2) Do inorder traversal of second tree and store the traversal in an auxiliary array ar2[]
3) Find intersection of ar1[] and ar2[].

Time complexity of this method is O(m+n) where m and n are number of nodes in first and second tree respectively.
This solution requires O(m+n) extra space.

Method 2 (Linear Time and limited Extra Space) We can find common elements in O(n) time and O(h1 + h2) extra space where h1 and h2 are heights of first and second BSTs respectively.

The idea is to use iterative inorder traversal. We use two auxiliary stacks for two BSTs. Since we need to find common elements, whenever we get same element, we add it to the sum .


```

class Solution:

    def solve(self, A, B):

        self.Hash_set = set();
        self.Sum = 0;

        self.PreOrderTraversal(A);
        self.PostOrderTraversal(B,1000000000+7);
        return self.Sum ;
    
    def PreOrderTraversal(self,node):
        if not node:
            return ;
        
        self.Hash_set.add(node.val);
        self.PreOrderTraversal(node.left);
        self.PreOrderTraversal(node.right);
    
    def PostOrderTraversal(self,node,mod):

        if not node :
            return ;

        self.PostOrderTraversal(node.left,mod);
        self.PostOrderTraversal(node.right,mod);

        if node.val in self.Hash_set:
            self.Sum = (self.Sum+node.val)%mod;


```
