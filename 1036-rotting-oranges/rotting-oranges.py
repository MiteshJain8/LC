class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dq = deque()
        fresh_cnt = 0
        time = -1
        dirs = ((-1,0), (0,1), (1,0), (0,-1))
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    dq.append((i, j))
                elif grid[i][j] == 1:
                    fresh_cnt += 1
        if not fresh_cnt:
            return 0
        while dq:
            l = len(dq)
            time += 1
            for _ in range(l):
                i, j = dq.popleft()
                for dx, dy in dirs:
                    x, y = i+dx, j+dy
                    if 0 <= x < m and 0 <= y < n and grid[x][y] == 1:
                        grid[x][y] = 2
                        dq.append((x, y))
                        fresh_cnt -= 1
        return -1 if fresh_cnt else time