### Top View of BT

https://practice.geeksforgeeks.org/problems/top-view-of-binary-tree/1


```

class Solution:

    def solve(self, A):
        if A == None:
            return [];
            
        self.HashMap = dict();
        
        return self.levelOrderTraversal(A);
        
    def levelOrderTraversal(self,node):
        
        top_view = [];
        horizontal_distance = 10**4;
        
        from collections import deque;
        queue = deque([]);
        queue.append([horizontal_distance, node]);
        
        while queue:
            
            horizontal_distance, node = queue.popleft();

            if horizontal_distance not in self.HashMap:
                self.HashMap[horizontal_distance] = [node.val];
                top_view.append(node.val);
                
            if node.left:
                queue.append([horizontal_distance-1,node.left]);
                
            if node.right:
                queue.append([horizontal_distance+1,node.right]);
        
        return top_view;
        


```
