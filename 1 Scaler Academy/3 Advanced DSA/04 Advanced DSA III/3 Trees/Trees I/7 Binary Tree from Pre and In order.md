### Construct Binary Tree from PreOrder and Inorder

https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

**Solution Approach**

  Focus on the preorder traversal to begin with. 
  The first element in the traversal will definitely be the root. 
  Based on this information, can you identify the elements in the left subtree
  and right subtree ? ( Hint : Focus on inorder traversal and root information )

  Once you do that, your problem has now been reduced to a smaller set. Now you 
  have the inorder and preorder traversal for the left and right subtree and you
  need to figure them out. 
  Divide and conquer. 

  Bonus points if you can do it without recursion.

```

class Solution:

	def buildTree(self, preorder, inorder):

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

        
		

