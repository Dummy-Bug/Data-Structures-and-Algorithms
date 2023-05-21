https://leetcode.com/problems/critical-connections-in-a-network/description/

### Problem Description 

There are n servers numbered from 0 to n - 1 connected by undirected server-to-server connections forming a network where connections[i] = [ai, bi] represents a connection between servers ai and bi. Any server can reach other servers directly or indirectly through the network.

A critical connection is a connection that, if removed, will make some servers unable to reach some other server.

Return all critical connections in the network in any order.

 

Example 1:


Input: n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
Output: [[1,3]]
Explanation: [[3,1]] is also accepted.
Example 2:

Input: n = 2, connections = [[0,1]]
Output: [[0,1]]
 

Constraints:

2 <= n <= 105
n - 1 <= connections.length <= 105
0 <= ai, bi <= n - 1
ai != bi
There are no repeated connections.

```


from collections import defaultdict;

class Solution:
    def __init__(self):
        self.graph = defaultdict(list);
        self.time  = 0;
        self.bridges  = [];

    def criticalConnections(self, n: int, connections: List[List[int]]):
        
        self.lrt      = [float("inf") for i in range(n)];
        self.discTime = [float("inf") for i in range(n)];
        self.visited  = [False for i in range(n)];
        
        for edge in connections:
            self.graph[edge[0]].append(edge[1]);
            self.graph[edge[1]].append(edge[0]);
            
        return self.dfs(0,-1);
    
    def dfs(self,src,parent):
        self.lrt[src] = self.discTime[src] = self.time;
        self.time += 1;
        self.visited[src] = True;

        for dst in self.graph[src]:
            if dst == parent:
                continue;
            if self.visited[dst] == False:
                self.dfs(dst,src);
                # now the dfs(v) has completed done and dusted;
                self.lrt[src] = min(self.lrt[src],self.lrt[dst]);
                if self.lrt[dst] > self.discTime[src]:
                    # if lowest reachable time of adjacent node is
                    # more than discovery/insertion time of current node
                    # then it means there is no other way of reaching to 
                    # adjacent node without currnt src node;
                    self.bridges.append([src,dst]);
            else:
                # if dst is already visited then obviously bridge is
                #  not possible so just update the lrt;
                self.lrt[src] = min(self.lrt[src],self.lrt[dst]);
        return self.bridges;

        
    
    
    ```
