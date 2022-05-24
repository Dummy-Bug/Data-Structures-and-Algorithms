# https://leetcode.com/problems/clone-graph/
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        if not node:
            return
        visited = dict()
        return self.dfs(node,visited)
    
    def dfs(self,node,visited):
        
        New_node = Node(node.val)
        
        visited[node] = New_node
        
        for padosi in node.neighbors:
            
            if padosi in visited:
                New_node.neighbors.append(visited[padosi])
            else:
                New_node.neighbors.append(self.dfs(padosi,visited))
                
        
        return New_node