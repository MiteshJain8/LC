class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(i,j):
            cnt = 1
            grid[i][j] = 0
            for dx,dy in dirs:
                x, y = i+dx, j+dy
                if 0 <= x < m and 0 <= y < n and grid[x][y]:
                    cnt += dfs(x,y)
            return cnt

        res = 0
        m, n = len(grid), len(grid[0])
        dirs = [(0,1), (1,0), (0,-1), (-1,0)]
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    res = max(res, dfs(i,j))
        return res