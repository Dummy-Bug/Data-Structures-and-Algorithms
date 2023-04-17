### Problem Description 

Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

 

Example 1:


Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]
Example 2:

Input: preorder = [-1], inorder = [-1]
Output: [-1]
 

Constraints:

1 <= preorder.length <= 3000
inorder.length == preorder.length
-3000 <= preorder[i], inorder[i] <= 3000
preorder and inorder consist of unique values.
Each value of inorder also appears in preorder.
preorder is guaranteed to be the preorder traversal of the tree.
inorder is guaranteed to be the inorder traversal of the tree.


```


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:


        self.Hash_map = dict();

        for i in range(len(inorder)):
            self.Hash_map[inorder[i]] = i;
        
        return self.constructTree(preorder,inorder,0,len(preorder)-1,0,len(inorder)-1);
    
    def constructTree(self,preorder,inorder,Ps,Pe,Is,Ie):

        if Ps > Pe:
            return None;
        node  = TreeNode(preorder[Ps]);
        index = self.Hash_map[node.val];

        node.left  = self.constructTree(preorder,inorder,Ps+1,Ps+index-Is,Is,index-1);
        node.right = self.constructTree(preorder,inorder,Ps+index-Is+1,Pe,index+1,Ie);

        return node;


```
