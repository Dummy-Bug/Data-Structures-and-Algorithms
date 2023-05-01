class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]):
        
        n = len(rooms)
        self.visited = [False for j in range(n)]
        
        return self.bfs(rooms,0,n)
    
    def bfs(self,rooms,u,n):
        
        from collections import deque
        q = deque()
        
        self.count = 1
        q.append(u)
        
        while q:
            u = q.popleft()
            
            for v in rooms[u]:
                
                if self.visited[v] == False:
                    self.count += 1
                    q.append(v)
                    
            self.visited[u] = True      
            
        return self.count == n
    