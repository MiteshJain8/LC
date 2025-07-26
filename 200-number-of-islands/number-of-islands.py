class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def bfs(u, v):
            if grid[u][v] == '0':
                return False

            pq = deque([(u,v)])
            grid[u][v] = '0'
            while pq:
                x, y = pq.popleft()
                for dx, dy in dirs:
                    nx, ny = x+dx, y+dy
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == '1':
                        pq.append((nx,ny))
                        grid[nx][ny] = '0'

            return True
            
        m = len(grid)
        n = len(grid[0])
        res = 0
        dirs = [(0,1), (0, -1), (1,0), (-1,0)]
        for i in range(m):
            for j in range(n):
                if bfs(i, j):
                    res += 1

        return res