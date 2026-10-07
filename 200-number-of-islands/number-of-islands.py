class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def bfs(a, b):
            dq = deque([(a,b)])
            visited[a][b] = True
            while dq:
                a, b = dq.popleft()
                for dx, dy in sides:
                    x = a + dx
                    y = b + dy
                    if m <= x or x < 0 or n <= y or y < 0:
                        continue
                    if grid[x][y] == "1" and not visited[x][y]:
                        visited[x][y] = True
                        dq.append((x,y))
            return

        def dfs(a, b):
            visited[a][b] = True
            for dx, dy in sides:
                x = a + dx
                y = b + dy
                if m <= x or x < 0 or n <= y or y < 0:
                    continue
                if grid[x][y] == "1" and not visited[x][y]:
                    dfs(x,y)
            return

        m, n = len(grid), len(grid[0])
        sides = [(0,1), (0,-1), (-1,0), (1,0)]
        res = 0
        visited = [[False for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and not visited[i][j]:
                    res += 1
                    bfs(i, j)
        return res
