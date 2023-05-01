### Check if Tree is Height Balanced or Not:-

https://www.interviewbit.com/problems/balanced-binary-tree/

**Solution Approach**

> A tree is balanced if :
1) Left subtree is balanced
2) Right subtree is balanced
3) The difference in the height of the left and right subtree is at most 1.

Can you think of a way to simulate that with recursion?
Note that depth of a tree can also be calculated recursively as max(depth(rightSubtree), depth(leftSubtree)) + 1



```

class Solution:

    def isBalanced(self, A):
        
        result = self.helper(A);
        return 1 if result != -1 else 0;
    
    def helper(self,node):
        
        if node == None:
            return 0;
        
        left_depth  = self.helper(node.left);
        right_depth = self.helper(node.right);
        
        if left_depth == -1 or right_depth == -1:
            return -1;
        if abs(left_depth-right_depth) < 2:
            return 1 + max(left_depth,right_depth);
        else:
            return -1

```
