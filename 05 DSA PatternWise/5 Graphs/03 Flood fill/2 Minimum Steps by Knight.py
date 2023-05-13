class Solution:
    
	def minStepToReachTarget(self, KnightPos, TargetPos, n):
	    
		self.color    = [['white' for i in range(n)] for j in range(n)]
		u , v = KnightPos[0],KnightPos[1]
		return self.bfs(u-1,v-1,n)
	
	def bfs(self,u,v,n):
	    
		from collections import deque
		q = deque()
	    q.append([u,v,0])
	    self.color[u][v] = 'grey'
	    
	    while q:
            x,y,distance = q.popleft()
            
            if x == TargetPos[0]-1 and y == TargetPos[1]-1:
                return distance
                
	        for next_pos in [(x-2, y-1) , (x-2, y+1) , (x-1, y-2) , (x-1, y+2) , (x+2, y-1) , (x+2, y+1) , (x+1, y-2) , (x+1, y+2) ]:
		        u, v  = next_pos
		        if (u >= 0 and v >= 0 and u < n  and v < n) :
		                
		            if self.color[u][v] == 'white':
		                self.color[u][v] = 'grey'
		                q.append([u,v,distance+1])
		                
		return -1     
