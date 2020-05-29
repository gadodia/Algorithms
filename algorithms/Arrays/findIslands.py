'''
This problem was recently asked by LinkedIn:

Given a 2-dimensional grid consisting of 1's (land blocks) and 0's (water blocks), count the number of islands present in the grid. The definition of an island is as follows:
1.) Must be surrounded by water blocks.
2.) Consists of land blocks (1's) connected to adjacent land blocks (either vertically or horizontally).
Assume all edges outside of the grid are water.

Example:
Input: 
10001
11000
10110
00000

Output: 3
'''

class Solution(object):

    def sinkIsland(self, grid, r, c):        
        grid[r][c] = 0
        if (r - 1) > 0 and grid[r-1][c] == 1:
            self.sinkIsland(grid, r-1, c)
        if (r + 1) < len(grid) and grid[r+1][c] == 1:
            self.sinkIsland(grid, r+1, c)
        if (c-1) > 0 and grid[r][c-1] == 1:
            self.sinkIsland(grid, r, c-1)
        if (c+1) < len(grid[0]) and grid[r][c+1] == 1:
            self.sinkIsland(grid, r, c+1)
        return
    
    def numIslands(self, grid):
        if not grid:
            return False
        islandcount = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    islandcount += 1
                    self.sinkIsland(grid, r, c)
        return islandcount


        

grid = [[1, 1, 0, 0, 0],
        [0, 1, 0, 0, 1],
        [1, 0, 0, 1, 1],
        [0, 0, 0, 0, 0]]
print(Solution().numIslands(grid))
# 3

