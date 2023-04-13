### Problem Description

Given any source point, (C, D) and destination point, (E, F) on a chess board of size A x B, we need to find whether Knight can move to the destination or not.


The above figure details the movements for a knight ( 8 possibilities ).

If yes, then what would be the minimum number of steps for the knight to move to the said point. If knight can not move from the source point to the destination point, then return -1.

NOTE: A knight cannot go out of the board.



Problem Constraints
1 <= A, B <= 500



Input Format
The first argument of input contains an integer A.
The second argument of input contains an integer B.
The third argument of input contains an integer C.
The fourth argument of input contains an integer D.
The fifth argument of input contains an integer E.
The sixth argument of input contains an integer F.



Output Format
If it is possible to reach the destination point, return the minimum number of moves.
Else return -1.



Example Input
Input 1:

 A = 8
 B = 8
 C = 1
 D = 1
 E = 8
 F = 8
Input 2:

 A = 2
 B = 4
 C = 2
 D = 1
 E = 4
 F = 4


Example Output
Output 1:

 6
Output 2:

 -1


Example Explanation
Explanation 1:

 The size of the chessboard is 8x8, the knight is initially at (1, 1) and the knight wants to reach position (8, 8).
 The minimum number of moves required for this is 6.
Explanation 2:

 It is not possible to move knight to position (4, 4) from (2, 1)
 
**Solution Approach**

A knight can move to 8 positions from (x,y). 

(x, y) -> 
    (x + 2, y + 1)  
    (x + 2, y - 1)
    (x - 2, y + 1)
    (x - 2, y - 1)
    (x + 1, y + 2)
    (x + 1, y - 2)
    (x - 1, y + 2)
    (x - 1, y - 2)

Corresponding to the knight's move, we can define edges. 
(x,y) will have an edge to the 8 neighbors defined above. 

To find the shortest path, we just run a plain BFS

```

from collections import deque;
queue = deque();
import sys;
sys.setrecursionlimit(10**9);

class Solution:
 
    def knight(self, A, B, C, D, E, F):
        
        self.visited = [[False for j in range(B)]for i in range(A)];
        
        return self.bfsVisit(A,B,C-1,D-1,E-1,F-1);
    
    def bfsVisit(self,A,B,w,x,y,z):
        
        queue.append([w,x]);
        ans = 0; self.visited[w][x] = True;
        
        while queue:
            size = len(queue);

            for _ in range(size):
                w,x = queue.popleft();
                
                if w==y and x==z:
                    return ans;
                
                for i,j in [(w+2,x+1) , (w+2, x-1) , (w-2, x+1) , (w-2, x-1) , (w+1, x+2) , (w+1, x-2) , (w-1, x+2) , (w-1, x-2) ]:
                    
                    if i<A and i>=0 and j<B and j>=0:
                       
                        if self.visited[i][j] == False:
                            queue.append([i,j]);
                            self.visited[i][j] = True;
                
            ans += 1;
        # print(ans)
        return -1;
                    
# Code Seems correct but was giving error in some testCases                      

```
```

from collections import deque

class Solution:
    def get_neighbours(self, node, N, M):

        potential_nodes = [
            (node[0] + 2, node[1] + 1),  (node[0] + 1, node[1] + 2),
            (node[0] + 2, node[1] - 1),  (node[0] + 1, node[1] - 2),
            (node[0] - 2, node[1] + 1),  (node[0] - 1, node[1] + 2),
            (node[0] - 2, node[1] - 1),  (node[0] - 1, node[1] - 2),
        ]

        neighbours = []
        for potential_node in potential_nodes:
            if 0 <= potential_node[0] and 0 <= potential_node[1] and potential_node[0] < N and potential_node[1] < M:
                neighbours.append(potential_node)

        return neighbours

    def knight(self, N, M, x1, y1, x2, y2):
        x1 -= 1
        y1 -= 1
        x2 -= 1
        y2 -= 1

        # M columns, N row
        table_count = [[1000000000 for x in range(M)] for x in range(N)]
        table_visited = [[False for x in range(M)] for x in range(N)]

        table_count[x1][y1] = 0
        queue = deque([(x1, y1)])
        # breath search

        while len(queue) != 0:

            node = queue.pop()

            if table_visited[node[0]][node[1]]:
                continue

            # print node
            table_visited[node[0]][node[1]] = True

            neighbours = self.get_neighbours(node, N, M)
            for neighbour in neighbours:

                queue.appendleft(neighbour)
                table_count[neighbour[0]][neighbour[1]] = min(
                    table_count[neighbour[0]][neighbour[1]], table_count[node[0]][node[1]] + 1)

        if table_count[x2][y2] != 1000000000:
            return table_count[x2][y2]
        else:
            return -1

```
