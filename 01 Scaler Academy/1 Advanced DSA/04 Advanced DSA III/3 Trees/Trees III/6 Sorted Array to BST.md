### Problem Description

Given an array where elements are sorted in ascending order, convert it to a height Balanced Binary Search Tree (BBST).

Balanced tree : a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.



Problem Constraints
1 <= length of array <= 100000



Input Format
First argument is an integer array A.



Output Format
Return a root node of the Binary Search Tree.



Example Input
Input 1:

 A : [1, 2, 3]
Input 2:

 A : [1, 2, 3, 5, 10]


Example Output
Output 1:

      2
    /   \
   1     3
Output 2:

      3
    /   \
   2     5
  /       \
 1         10


Example Explanation
Explanation 1:

 You need to return the root node of the Binary Tree.
 
 
 **Solution Approach**
 
 For a BST, all values lower than the root go in the left part of the root, and all values higher go in the right part of the root.
To balance the tree, we will need to make sure we distribute the elements almost equally in the left and right parts.
So we choose the mid part of the array as the root and divide the elements around it.

Things to take care of :
1) Are you passing a copy of the array around, or are you only passing around a reference?
2) Are you dividing the array before passing it onto the next function call or are you just specifying the start and end index?


 ```
 
 import sys 
sys.setrecursionlimit(10**6);

class Solution:

    def sortedArrayToBST(self, A):   
        return self.dfs(A,0,len(A));     
    
    def dfs(self,arr,l,r):
        
        if l >= r:
            return None
            
        root_indx = (l+r)//2
        root = TreeNode(arr[root_indx])
            
        root.left  = self.dfs(arr,l,root_indx)
        root.right = self.dfs(arr,root_indx+1,r)
            
        return root
 
 ```
