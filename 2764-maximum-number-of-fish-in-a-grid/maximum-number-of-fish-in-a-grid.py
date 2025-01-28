class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        def bfs(i,j):
            q = deque([(i,j)])
            cnt = 0
            while q:
                r,c = q.popleft()
                cnt += grid[r][c]
                grid[r][c] = 0
                for dx,dy in dirs:
                    x, y = r+dx, c+dy
                    if 0 <= x < m and 0 <= y < n and grid[x][y]:
                        q.append((x,y))
            return cnt

        res = 0
        dirs = [(0,1), (1,0), (0,-1), (-1,0)]
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    res = max(res, bfs(i,j))
        return res