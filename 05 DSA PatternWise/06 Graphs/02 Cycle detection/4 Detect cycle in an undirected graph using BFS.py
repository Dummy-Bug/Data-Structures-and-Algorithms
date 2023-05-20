# can't solve it without predecessor array 
class Solution:
	def isCycle(self, V, adj):
		self.color = ['white']*V
		self.pred  = [-1]*V
		
		for i in range(V):
		    
		    if self.color[i] == 'white':
		        
		        if self.bfs(i,adj):
		            return True
		            
		return False
	
	def bfs(self,u,adj):
	    
	    from collections import deque
	    q = deque([])
	    q.append(u)
	    self.color[u] = 'grey'
	    
	    while q:
	        u = q.popleft()
	        for v in adj[u]:
	            
	            if self.color[v] == 'black' and self.pred[u] != v:
	                return True
	                
	            elif self.color[v] == 'white':
	                self.pred[v] = u
	                self.color[v] = 'grey'
	                q.append(v)
	                    
	        self.color[u] = 'black'
	       
	    return False
