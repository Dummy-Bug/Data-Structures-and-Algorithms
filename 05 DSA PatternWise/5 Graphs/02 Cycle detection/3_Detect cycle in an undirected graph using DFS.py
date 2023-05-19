# Can be solved without the predecessor array as we can take prev node as paramater and solve it easily
class Solution:
	def isCycle(self, V, adj):
	    
		self.pred  = [-1]*V
		self.color = ['white']*V
		
		for i in range(V):
		    if self.color[i] == 'white':
		        if self.dfs(i,adj):
		            return True
		return False
		        
	def dfs(self,u,adj):
	    self.color[u] = 'grey'
	    
		for v in adj[u]:
		    
		    if self.color[v] == 'grey' and self.pred[u] != v:
		        
		        return True
		        
		    elif self.color[v] == 'white':
		        self.pred[v] = u
		        if self.dfs(v,adj):
		            return True
		        
		self.color[u] = 'black'
		return False
