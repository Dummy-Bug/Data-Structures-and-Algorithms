class Solution:
    
    def canFinish(self, n: int, pre: List[List[int]]):
        from collections import deque
        from collections import defaultdict

        self.seen = set()
        self.q    = deque()
        self.graph = {}
        self.in_degree = {}
        
        for edge in pre:
            u,v = edge
            
            if u not in self.graph:
                self.graph[u] = []
            self.graph[u].append(v)
            
            if v not in self.in_degree:
                self.in_degree[v] = 0
            self.in_degree[v] += 1
    
        for i in range(n):
            if i not in self.in_degree:
                self.q.append(i)
                
        self.bfs(pre)
        return ( len(self.seen)== n ) 
    
    def bfs(self,pre):
        
        while self.q:
            
            u = self.q.popleft()
            self.seen.add(u)
            
            if u not in self.graph:
                continue
                
            for padosi in self.graph[u]:
                
                if padosi not in self.seen :
                    self.in_degree[padosi] -= 1
                    
                    if self.in_degree[padosi] == 0:
                        self.q.append(padosi)
        