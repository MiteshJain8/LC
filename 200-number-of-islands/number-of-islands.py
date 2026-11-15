class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(x, y):
            grid[x][y] = "0"
            for dx, dy in dirs:
                p, q = x+dx, y+dy
                if 0 <= p < m and 0 <= q < n and grid[p][q] == "1":
                    dfs(p, q)

        m, n, res = len(grid), len(grid[0]), 0
        dirs = ((-1,0), (0,1), (0,-1), (1,0))
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    res += 1
                    dfs(i, j)
        return res