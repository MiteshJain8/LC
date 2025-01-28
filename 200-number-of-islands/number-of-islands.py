class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i,j):
            grid[i][j] = '0'
            for dx,dy in dirs:
                x, y = i+dx, j+dy
                if 0 <= x < m and 0 <= y < n and grid[x][y] == '1':
                    dfs(x,y)

        res = 0
        m, n = len(grid), len(grid[0])
        dirs = [(0,1), (1,0), (0,-1), (-1,0)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    dfs(i,j)
                    res += 1
        return res