class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        m, n = len(isWater), len(isWater[0])
        q = deque([])
        for i in range(m):
            for j in range(n):
                if isWater[i][j]:
                    isWater[i][j] = 0
                    q.append((0, i, j))
                else: isWater[i][j] = -1
        d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while q:
            h, x, y = q.popleft()
            for dx, dy in d:
                a, b = x + dx, y + dy
                if 0 <= a < m and 0 <= b < n and isWater[a][b] == -1:
                    isWater[a][b] = h+1
                    q.append((h+1, a, b))
        return isWater