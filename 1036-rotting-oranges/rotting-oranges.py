class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dirs = [(-1,0), (0,1), (1,0), (0,-1)]
        res = -1
        change = True
        new_grid = copy.deepcopy(grid)
        while change:
            change = False
            res += 1
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 2:
                        for dx, dy in dirs:
                            x, y = i+dx, j+dy
                            if 0 <= x < m and 0 <= y < n and grid[x][y] == 1:
                                change = True
                                new_grid[x][y] = 2
            grid = new_grid
            new_grid = copy.deepcopy(grid)
        for row in grid:
            if 1 in row:
                return -1
        return res