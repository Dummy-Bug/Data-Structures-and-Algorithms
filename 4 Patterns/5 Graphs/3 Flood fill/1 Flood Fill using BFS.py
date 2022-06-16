class Solution:
    from collections import deque
    
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        
        m = len(image) 
        n = len(image[0])
        
        self.visited_pixel = [[False for j in range(n)] for i in range(m)]

        return self.bfs(image,sr,sc,m,n,newColor)
        
    def bfs(self,image,sr,sc,m,n,newColor):
        
        q = deque()
        q.append([sr,sc])
        old_color = image[sr][sc]
        image[sr][sc] = newColor
        
        while q:
            x, y = q.popleft()
            
            for u,v in [ [x-1,y], [x+1,y], [x,y-1], [x,y+1] ]:
                
                if u >= 0 and v >= 0 and u < m and v < n:
                    
                    if image[u][v] == old_color and self.visited_pixel[u][v] == False:
                        
                        image[u][v] = newColor
                        self.visited_pixel[u][v] = True
                        q.append([u,v])
                        
        return image
        