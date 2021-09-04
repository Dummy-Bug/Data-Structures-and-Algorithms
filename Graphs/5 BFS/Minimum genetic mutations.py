class Solution:
    
    def __init__(self):
        
        from collections import defaultdict
        self.graph = defaultdict(lambda:[])
        
    def check(self,u,v):
        i = count = 0
        
        while i < len(u):
            if u[i] != v[i]:
              
                count = count + 1
                if count > 1:
                    return False
            i = i + 1
        return True
        
    def bfs(self,start,end):
        
        from collections import deque
        q = deque()
        q.append(start)
        
        while q:
            ln = len(q)
            
            for i in range(ln): 
                
                u = q.popleft()
                
                self.visited[u] = True
                if u == end:
                    return self.result
                
                for v in self.graph[u]:
                    
                    if self.visited[v] == False:
                        q.append(v)
        
            self.result = self.result + 1
        return -1
        
        
    def minMutation(self, start: str, end: str, bank: List[str]):
        
        if end not in bank:
            return -1
        for u in [start] + bank:
            for v in bank:
                
                if v!=u and self.check(u,v):
                    self.graph[u].append(v)
         
        self.result = 0
        self.visited = dict()
        
        for word in [start] + bank:
            self.visited[word] = False
        
        return self.bfs(start,end)