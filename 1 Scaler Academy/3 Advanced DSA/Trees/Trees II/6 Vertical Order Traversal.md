### Vertical Order Traversal of BT

https://www.interviewbit.com/problems/vertical-order-traversal-of-binary-tree/

**Notes**

> Important question as it helps in finding the Top View of Binary Tree

```

class Solution:

    def verticalOrderTraversal(self, A):
        
        if A == None:
            return [];
            
        self.HashMap = dict();
        
        min_dist,max_dist = self.levelOrderTraversal(A);

        result = [];

        for distance in range(min_dist,max_dist+1):
            result.append( self.HashMap[distance] );
        
        return result;
        
    def levelOrderTraversal(self,node):
        
        horizontal_distance = 10**4;
        
        from collections import deque;
        queue = deque([]);
        min_dist,max_dist = float('inf'),float('-inf');
        
        queue.append([horizontal_distance, node]);
        
        while queue:
            
            horizontal_distance, node = queue.popleft();
            
            min_dist = min(min_dist,horizontal_distance);
            max_dist = max(max_dist,horizontal_distance);

            if horizontal_distance not in self.HashMap:
                self.HashMap[horizontal_distance] = [];
                
            self.HashMap[horizontal_distance].append(node.val);
                
            if node.left:
                queue.append([horizontal_distance-1,node.left]);
                
            if node.right:
                queue.append([horizontal_distance+1,node.right]);
        
        return [min_dist,max_dist];


```
