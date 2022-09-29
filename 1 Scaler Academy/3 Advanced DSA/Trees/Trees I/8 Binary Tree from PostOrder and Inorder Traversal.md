### Construct Bt from Postorder and Inorder Traversal

https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/


```

class Solution:

	def buildTree(self,inorder,postorder):

        self.Hash_map = dict();

        for i in range(len(inorder)):
            self.Hash_map[inorder[i]] = i;
        
        return self.constructTree(postorder,inorder,0,len(postorder)-1,0,len(inorder)-1);
    
    def constructTree(self,postorder,inorder,Ps,Pe,Is,Ie):

        if Ps > Pe or Is > Ie:
            return None;
        node   = TreeNode(postorder[Pe]);
        index  = self.Hash_map[node.val];
        length = index-Is;
        node.left  = self.constructTree(postorder,inorder,Ps,Ps+length-1,Is,index-1);
        node.right = self.constructTree(postorder,inorder,Ps+length,Pe-1,index+1,Ie);

        return node;


```
