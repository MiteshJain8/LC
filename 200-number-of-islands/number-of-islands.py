class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(a, b):
            visited[a][b] = True
            sides = [(0,1), (0,-1), (-1,0), (1,0)]
            for dx, dy in sides:
                x = a + dx
                y = b + dy
                if m <= x or x < 0 or n <= y or y < 0:
                    continue
                if grid[x][y] == "1" and not visited[x][y]:
                    dfs(x,y)
            return

        m, n = len(grid), len(grid[0])
        res = 0
        visited = [[False for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and not visited[i][j]:
                    res += 1
                    dfs(i, j)
        return res
