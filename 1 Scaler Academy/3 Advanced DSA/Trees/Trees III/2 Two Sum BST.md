### Two Sum input is BST

https://leetcode.com/problems/two-sum-iv-input-is-a-bst/

**notes**

-> All possible solutions 
-> https://leetcode.com/problems/two-sum-iv-input-is-a-bst/discuss/1420711/C%2B%2BJavaPython-3-solutions%3A-HashSet-Stack-Python-yield-Solutions-O(H)-space

```

class Solution:

	def t2Sum(self, A, B):

        self.Hash_set = set();

        return self.traversal(A,B);
    
    def traversal(self,node,target):
        if not node:
            return;
        
        if target-node.val in self.Hash_set:
            return 1;
        
        self.Hash_set.add(node.val);

        if self.traversal(node.left,target) or self.traversal(node.right,target):
            return 1;
        return 0; 


```
