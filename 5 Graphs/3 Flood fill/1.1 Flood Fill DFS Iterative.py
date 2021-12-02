class Solution:
	def floodFill(self, image, sr, sc, newColor):
	    
	    m = len(image)
	    n = len(image[0])
	    
	    self.image       = image
	    self.new_color   = newColor
	    self.old_color   = image[sr][sc]
		self.visited = [[ False for j in range(n)] for i in range(m)]
		
		self.dfs(sr,sc,m,n)
		return self.image
		    
	def dfs(self,x,y,m,n):
	    
	    self.visited[x][y] = True
	    image[x][y] = self.new_color
	    
	    for i , j in [(x-1,y), (x+1,y), (x,y-1), (x,y+1)]:
	        
	        if i >= 0 and j >= 0 and i < m and j < n :
	            
	            if image[i][j] == self.old_color and self.visited[i][j] == False:
	                self.dfs(i,j,m,n)
	