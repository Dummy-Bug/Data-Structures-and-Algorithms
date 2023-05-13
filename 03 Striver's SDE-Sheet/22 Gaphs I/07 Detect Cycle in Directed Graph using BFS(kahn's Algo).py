# https://practice.geeksforgeeks.org/problems/detect-cycle-in-a-directed-graph/1#
class Solution:
    def isCyclic(self, V, adj):
        from collections import deque
        q = deque([])
        self.dx = {}
        self.visited = 0
        
        for neighbor_list in adj:
            for neighbor in neighbor_list:
                if neighbor not in self.dx:
                    self.dx[neighbor]  = 1
                else:
                    self.dx[neighbor] += 1
        # dx contains all the in_degrees of a vertex
        for i in range(V):
            if i not in self.dx:
                q.append(i)
        while q:
            vertex = q.popleft()
            self.visited += 1
            
            for neighbor in adj[vertex]:
                
                self.dx[neighbor] -= 1 # decrease the in_degree
                if self.dx[neighbor] == 0:
                    q.append(neighbor)
        return self.visited != V # if equal then means no cycle