class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def bfs(x, y):
            grid[x][y] = "0"
            dq = deque([(x,y)])
            while dq:
                a, b = dq.popleft()
                for dx, dy in dirs:
                    p, q = a+dx, b+dy
                    if 0 <= p < m and 0 <= q < n and grid[p][q] == "1":
                        dq.append((p,q))
                        grid[p][q] = "0"

        m, n, res = len(grid), len(grid[0]), 0
        dirs = ((-1,0), (0,1), (0,-1), (1,0))
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    res += 1
                    bfs(i, j)
        return res