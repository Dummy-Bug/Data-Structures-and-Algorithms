### Problem Description

Given a binary tree. Check whether the given tree is a Sum-binary Tree or not.

Sum-binary Tree is a Binary Tree where the value of a every node is equal to sum of the nodes present in its left subtree and right subtree.

An empty tree is Sum-binary Tree and sum of an empty tree can be considered as 0. A leaf node is also considered as SumTree.

Return 1 if it sum-binary tree else return 0.



Problem Constraints
1 <= length of the array <= 100000

0 <= node values <= 50



Input Format
The only argument given is the root node of tree A.



Output Format
Return 1 if it is sum-binary tree else return 0.



Example Input
Input 1:

       26
     /    \
    10     3
   /  \     \
  4   6      3
Input 2:

       26
     /    \
    10     3
   /  \     \
  4   6      4


Example Output
Output 1:

 1
Output 2:

 0


Example Explanation
Explanation 1:

 All leaf nodes are considered as SumTree. 
 Value of Node 10 = 4 + 6.
 Value of Node 3 = 0 + 3 
 Value of Node 26 = 20 + 6 
Explanation 2:

 Sum of left subtree and right subtree is 27 which is not equal to the value of root node which is 26.
 
 **Solution Approach**
 
 A simple solution is to check for every node is their sub-tree sum is equal to value of that node. But it will take O(n2)

An efficient approach is to store sum of subtree at the node, so we don’t need to calculate it again and again.

1) If the node is a leaf node then sum of subtree rooted with this node is equal to value of this node.
2) If the node is not a leaf node then sum of subtree rooted with this node is twice the value of this node (Assuming that the tree rooted with this node is SumTree).

If all nodes are sumTree return 1 else return 0.

 
 ```
 
 def isLeaf(node):
    if(node == None):
        return 0
    if(node.left == None and node.right == None):
        return 1
    return 0

def isSumTree(node):

    if(node == None or isLeaf(node)):
        return 1
        
    if( isSumTree(node.left) and isSumTree(node.right)):
        if(node.left == None):
            ls = 0
        elif(isLeaf(node.left)):
            ls = node.left.val
        else:
            ls = 2 * (node.left.val)
        if(node.right == None):
            rs = 0
        elif(isLeaf(node.right)):
            rs = node.right.val
        else:
            rs = 2 * (node.right.val)
        return(node.val == ls + rs)
    
    return 0
class Solution:

    def solve(self, A):
        if(isSumTree(A)):
            return 1
        return 0
 
 ```
