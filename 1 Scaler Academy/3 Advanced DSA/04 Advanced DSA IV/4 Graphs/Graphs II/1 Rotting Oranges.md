https://leetcode.com/problems/rotting-oranges/description/ 


**SOlution Approach**

  Every turn, the rotting spreads from each rotting orange to other adjacent oranges.
  Initially, the rotten oranges have ‘depth’ 0, and every time they rot a neighbor,
  the neighbors have 1 more depth. We want to know the largest possible depth.

  Use multi-source BFS to achieve this with all cells containing rotten oranges as starting nodes.
  At the end check if there are fresh oranges left or not.


```

class Solution:

    def solve(self, grid):

        row = len(grid)
        col = len(grid[0])
        l = 0
        fresh_oranges = 0
        from collections import deque
        q = deque()
        
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 2: # finding the position of rotten orange
                    q.append((r,c,l))
                elif grid[r][c] == 1:
                    fresh_oranges += 1
        while q:
            r,c,l = q.popleft()
            for i,j in [r-1,c],[r+1,c],[r,c-1],[r,c+1]:
                if i>=0 and i<row and j>=0 and j <col and grid[i][j] == 1:
                    q.append((i,j,l+1))
                    fresh_oranges -= 1
                    grid[i][j] = 0
        
        if fresh_oranges == 0:
            return l
        else:
            return -1


```
