# https://practice.geeksforgeeks.org/problems/depth-first-traversal-for-a-graph/1#
class Solution:
    
    #Function to return a list containing the DFS traversal of the graph.
    def dfsOfGraph(self, V, adj):
        
        visited = dict()
        result  = []
        self.dfs(0,adj,visited,result)
        return result
    
    def dfs(self,vertex,neighbors,visited,result):
        
        result.append(vertex)
        visited[vertex] = True
        
        for neighbor in neighbors[vertex]:
            if neighbor not in visited:
                self.dfs(neighbor,neighbors,visited,result)