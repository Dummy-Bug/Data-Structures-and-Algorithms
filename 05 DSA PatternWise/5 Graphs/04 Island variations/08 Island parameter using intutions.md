https://leetcode.com/problems/island-perimeter/description/

Problem Description
You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

Example 1:

Input: grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]] Output: 16 Explanation: The perimeter is the 16 yellow stripes in the image above. Example 2:

Input: grid = [[1]] Output: 4 Example 3:

Input: grid = [[1,0]] Output: 4

Constraints:

row == grid.length col == grid[i].length 1 <= row, col <= 100 grid[i][j] is 0 or 1. There is exactly one island in grid.


```


class Solution:
    
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perim = 0
        h, w = len(grid), len(grid[0])

    # Iterate through each cell
        for row in range(0, h):
            for col in range(0, w):

            # Is this a land cell?
                if grid[row][col] == 1:

                # Top edge
                    if row == 0 or grid[row - 1][col] == 0:
                        perim += 1

                # Bottom edge
                    if row == h - 1 or grid[row + 1][col] == 0:
                        perim += 1

                # Left edge
                    if col == 0 or grid[row][col - 1] == 0:
                        perim += 1

                # Right edge
                    if col == w - 1 or grid[row][col + 1] == 0:
                        perim += 1

        return perim

# Always Always see the solution of leetcode


```
