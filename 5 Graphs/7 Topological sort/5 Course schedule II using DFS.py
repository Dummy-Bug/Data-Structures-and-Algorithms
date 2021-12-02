class Solution:
    
    def findOrder(self, n: int, pre: List[List[int]]) -> List[int]:
     # keep on appenidng the finished nodes in queue ,if cycle is found anywhere return []
        

        self.graph = {i:[] for i in range(n)}    
        for edge in pre:            # edge is from b-->a, bcz it's given that we have to finish b before a.
            a, b = edge[0], edge[1] 

            self.graph[b].append(a) # appending outgoing edges of vertex b
        
        self.color  = ['white' for i in range(n)]
        from collections import deque
        self.result = deque() # taking queue instead of stack so that we can insert in the beginning in O(1)
                         
        for i in range(n):
            if self.color[i] == 'white':
            
                if self.dfs(i) == []: # if encounter False in any of the function call return the answer 
                    return []
        return self.result
            
    def dfs(self,source):
        self.color[source] = 'grey'
        
        for padosi in self.graph[source]:
            
            if self.color[padosi] == 'grey': # if encounter unfinished edge cycle is found.
                return []                 
            
            elif self.color[padosi] == 'white':
                if self.dfs(padosi) == []:
                    return []
        
        self.color[source] = 'black'
        self.result.appendleft(source) # O(1)
        
        return self.result
                
        
            

        
        
         
        
        
        
        
        