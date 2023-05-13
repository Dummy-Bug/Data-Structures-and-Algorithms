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

# Always see the solution of leetcode
