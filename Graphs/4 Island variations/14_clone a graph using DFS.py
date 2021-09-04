class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        if not node :
            return
        self.visited = {}
        
        return self.dfs(node)
        
    def dfs(self,node):
        
        if node in self.visited:
            return self.visited[node]
        
        new_node = Node(node.val,[])
        self.visited[node] = new_node 
        
        for padosi in node.neighbors:
            
                new_node.neighbors.append(self.dfs(padosi))
                    
        return new_node