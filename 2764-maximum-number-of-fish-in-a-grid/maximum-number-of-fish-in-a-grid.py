class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        def dfs(i,j):
            cnt = grid[i][j]
            grid[i][j] = 0
            for x,y in dirs:
                dx, dy = i+x, j+y
                if 0 <= dx < m and 0 <= dy < n and grid[dx][dy]:
                    cnt += dfs(dx,dy) 
            return cnt

        res = 0
        dirs = [(0,1), (1,0), (0,-1), (-1,0)]
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    res = max(res, dfs(i,j))
        return res