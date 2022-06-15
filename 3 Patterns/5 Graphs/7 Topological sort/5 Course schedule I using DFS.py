class Solution:
    def canFinish(self, n: int, pre: List[List[int]]):
        
          # problem is nothing but finding a cycle in directed graph
          # we can use either DFS or BFS(kahn's algo).


# let's  make the graph 
        self.graph = {i:[] for i in range(n)}    
        for edge in pre:            # edge is from b-->a, bcz it's given that we have to finish b before a.
            a, b = edge[0], edge[1] 

            self.graph[b].append(a) # appending outgoing edges of vertex b
        
        self.color = ['white' for i in range(n)]
        for i in range(n):
            if self.color[i] == 'white':
            
                if self.dfs(i) == False: # if encounter False in any of the function call return the answer 
                    return False
        return True
            
    def dfs(self,source):
        self.color[source] = 'grey'
        
        for padosi in self.graph[source]:
            
            if self.color[padosi] == 'grey': # if encounter unfinished edge cycle is found.
                return False                 # returning False means can't finish all the courses
            
            elif self.color[padosi] == 'white':
                if self.dfs(padosi) == False:
                    return False
        
        self.color[source] = 'black'
        return True
                
        
            

        
        