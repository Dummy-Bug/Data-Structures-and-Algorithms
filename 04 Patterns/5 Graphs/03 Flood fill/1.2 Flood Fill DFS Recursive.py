class Solution:
    from collections import deque
    
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        
        m = len(image) 
        n = len(image[0])
        
        self.old_color = image[sr][sc]
        self.new_color = newColor
        self.visited   = [[False for j in range(n)] for i in range(m)]
        
        self.dfs(image,sr,sc,m,n)
        return image
    
    def dfs(self,image,x,y,m,n):
        
        if self.visited[x][y] == True:
            return 
        self.visited[x][y] = True
        
        image[x][y] = self.new_color
        
        if x-1 >= 0 and image[x-1][y] == self.old_color:
            self.dfs(image,x-1,y,m,n)
            
        if y-1 >= 0 and image[x][y-1] == self.old_color:
            self.dfs(image,x,y-1,m,n)
            
        if x+1 < m and image[x+1][y]  == self.old_color:
            self.dfs(image,x+1,y,m,n)
        
        if y+1 < n and image[x][y+1] == self.old_color:
            self.dfs(image,x,y+1,m,n)