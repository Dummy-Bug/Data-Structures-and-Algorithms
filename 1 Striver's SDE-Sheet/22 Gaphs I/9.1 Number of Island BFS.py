# https://leetcode.com/problems/number-of-islands/
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 
        count = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1' :
                    count += 1
                    grid[row][col] = '0'
                    self.bfs(grid,row,col)
        return count
    def bfs(self,grid,row,col):
        from collections import deque
        q = deque()
        q.append((row,col))
        while q:
            row,col = q.popleft()
            for i,j in [(row-1,col),(row+1,col),(row,col+1),(row,col-1)]:
                if 0<=i and i<len(grid) and 0<=j and j<len(grid[0]):
                    if grid[i][j] == '1':
                        grid[i][j] = '0'
                        q.append((i,j))