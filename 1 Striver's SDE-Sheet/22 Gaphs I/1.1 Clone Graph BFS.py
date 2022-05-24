# https://leetcode.com/problems/clone-graph/
class Solution:
    from collections import deque
    
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        if not node:
            return
        
        visited = {}
        visited[node] = Node(node.val,[])
        
        return self.bfs(node,visited)
    
    def bfs(self,node,visited):

        queue = deque()
        queue.append(node)
        
        while queue:
            vertex = queue.popleft()
            
            for neighbor in vertex.neighbors:
                
                if neighbor not in visited:
                    
                    visited[neighbor] = Node(neighbor.val,[])
                    queue.append(neighbor)
                    
                visited[vertex].neighbors.append(visited[neighbor])
                
        return visited[node]