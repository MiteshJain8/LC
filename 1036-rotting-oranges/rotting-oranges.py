class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        fresh = 0
        res = 0
        dq = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    dq.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1
        if not fresh:
            return 0
        dirs = [(-1,0), (0,1), (1,0), (0,-1)]
        while dq:
            l = len(dq)
            flag = False
            for _ in range(l):
                a, b = dq.popleft()
                for dx, dy in dirs:
                    x, y = a+dx, b+dy
                    if 0 <= x < m and 0 <= y < n and grid[x][y] == 1:
                        grid[x][y] = 2
                        dq.append((x,y))
                        fresh -= 1
                        flag = True
            if flag:
                res += 1
        return -1 if fresh else res