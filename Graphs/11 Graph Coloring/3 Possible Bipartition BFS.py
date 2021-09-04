class Solution:
    def __init__(self):
        
        from collections import defaultdict,deque
        
        self.graph = defaultdict(lambda:[])
        
    def possibleBipartition(self, n: int, dislikes: List[List[int]]):
        
        self.visited = [False for i in range(n+1)]
        
        for edge in dislikes:
            u, v = edge[0], edge[1]
            self.graph[u].append(v)
            self.graph[v].append(u) # if a dislikes b then it means b dislikes a too.
            
        self.color = [-1 for i in range(n+1)]
        
        for i in range(n):
            
            if self.visited[i] == False:
                if self.bfs(i) == False:
                    return False
        return True
    
    def bfs(self,u):
        q = deque()
        q.append(u)
        self.color[u] = 0
        
        while q:
            ln = len(q)
            
            for _ in range(ln):
                
                u = q.popleft()
                self.visited[u] = True
                
                for v in self.graph[u]:
                    
                    if self.visited[v] == False:
                        
                        if self.color[v] == self.color[u]:
                            return False
                        
                        self.color[v] = (self.color[u] + 1)%2
                        q.append(v)
            
        return True
            
            