class Solution:
    def minimumEffortPath(self, heights: list[list[int]]) -> int:
        rows, cols = len(heights), len(heights[0])
        dirs = [(-1,0), (0,1), (0,-1), (1,0)]
        pq = [(0, 0, 0)]
        visit = [[False for _ in range(cols)] for _ in range(rows)]
        while pq:
            diff, i, j = heappop(pq)
            if visit[i][j]:
                continue
            if i == rows-1 and j == cols-1:
                return diff
            visit[i][j] = True
            for dx, dy in dirs:
                    x, y = i + dx, j + dy
                    if 0 <= x < rows and 0 <= y < cols and not visit[x][y]:
                        newDiff = max(diff, abs(heights[x][y] - heights[i][j]))
                        heappush(pq, (newDiff, x, y))

