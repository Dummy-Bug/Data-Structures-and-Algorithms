### BST nodes in a range

https://leetcode.com/problems/range-sum-of-bst/

**Solution Approach**

    The idea is to traverse the given binary search tree starting from the root.
    For every node being visited, check if this node lies in range,
    if yes, then add 1 to the result and recur for both of its children.
    If the current node is smaller than the low value of the range, then recur for the right child; else recur for the left child.


```

class Solution:

    def solve(self, A, B, C):
        self.Count = 0;

        self.NodesInRange(A,B,C);
        return self.Count;
    
    def NodesInRange(self,node,left_limit,right_limit):

        if not node:
            return;
        
        if left_limit<=node.val and right_limit>=node.val:
            self.Count += 1;
        
        if node.val > left_limit:
            self.NodesInRange(node.left,left_limit,right_limit);
        
        if node.val < right_limit:
            self.NodesInRange(node.right,left_limit,right_limit);



```
