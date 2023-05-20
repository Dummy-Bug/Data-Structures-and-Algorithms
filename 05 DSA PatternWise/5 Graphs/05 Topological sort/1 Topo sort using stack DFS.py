class Solution:
    
    # A recursive function used by topologicalSort
    def DFSUtil(self,adj,v,visited,stack):

        #marking the current vertex as visited.
        visited[v] = True

        #traversing over the adjacent vertices.
        for i in adj[v]:
            
            #if any vertex is not visited, we call the function recursively.
            if visited[i] == False:
                self.DFSUtil(adj,i,visited,stack)

        #pushing the current vertex into the stack.
        stack.append(v)
    
    #Function to return list containing vertices in Topological order.
    def topoSort(self, V, adj):
        
        #using boolean array to mark visited nodes and currently 
        #marking all the nodes as false.
        visited = [False]*V
        stack =[]

        #traversing over all the vertices.
        for i in range(V):
            
            #if the current vertex is not visited, we call the topo function.
            if visited[i] == False:
                self.DFSUtil(adj,i,visited,stack)

        #returning the stack.
        return stack[::-1]