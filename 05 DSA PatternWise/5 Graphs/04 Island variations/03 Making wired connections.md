https://leetcode.com/problems/number-of-operations-to-make-network-connected/description/

### problem Description

There are n computers numbered from 0 to n - 1 connected by ethernet cables connections forming a network where connections[i] = [ai, bi] represents a 
connection between computers ai and bi. Any computer can reach any other computer directly or indirectly through the network.

You are given an initial computer network connections. You can extract certain cables between two directly connected computers, and place them between any pair of disconnected computers to make them directly connected.

Return the minimum number of times you need to do this in order to make all the computers connected. If it is not possible, return -1.

 

Example 1:


Input: n = 4, connections = [[0,1],[0,2],[1,2]]
Output: 1
Explanation: Remove cable between computer 1 and 2 and place between computers 1 and 3.
Example 2:


Input: n = 6, connections = [[0,1],[0,2],[0,3],[1,2],[1,3]]
Output: 2
Example 3:

Input: n = 6, connections = [[0,1],[0,2],[0,3],[1,2]]
Output: -1
Explanation: There are not enough cables.
 

Constraints:

1 <= n <= 105
1 <= connections.length <= min(n * (n - 1) / 2, 105)
connections[i].length == 2
0 <= ai, bi < n
ai != bi
There are no repeated connections.
No two computers are connected by more than one cable.

```


class Solution:
    def graph(self,edge):
        u, v = edge[0], edge[1]
        
        self.list[u].append(v)
        self.list[v].append(u)
    
    def dfs(self,u):
        self.visited[u] = True
        
        for padosi in self.list[u]:
            
            if self.visited[padosi] == False:
                self.dfs(padosi)
        
    
    def makeConnected(self, n, connections):

       # take any graph of n vertices we need atleast n-1 edges to make it connected.
        if n > len(connections)+1:
            return -1
      # observe carefully problem is nothing but finding the number of connected components.       
        
        self.visited = [False for i in range(n)]

     # just make the graph and traverse it using DFS/BFS 
        self.list = {} 
        for i in range(n):
            self.list[i] = []
            
        for edge in connections:
            self.graph(edge)
        result = -1
        for vertex in range(n):
            if self.visited[vertex] == False:
                self.dfs(vertex)
                result = result + 1
        return result
        
        
        ```
