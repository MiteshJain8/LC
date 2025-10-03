class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        m, n = len(heightMap), len(heightMap[0])
        heap = []
        visit = [[False] * n for _ in range(m)]
        for i in range(m):
            for j in [0, n-1]:
                heappush(heap, (heightMap[i][j], i, j))
                visit[i][j] = True
        for j in range(1, n):
            for i in [0, m-1]:
                heappush(heap, (heightMap[i][j], i, j))
                visit[i][j] = True
        res = 0
        dirs = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        while heap:
            val, i, j = heappop(heap)
            for dx, dy in dirs:
                x, y = i + dx, j + dy
                if 0 <= x < m and 0 <= y < n and not visit[x][y]:
                    visit[x][y] = True
                    res += max(0, val - heightMap[x][y])
                    heappush(heap, (max(heightMap[x][y], val), x, y))

        return res