class Solution:
    def minimumEffortPath(self, heights: list[list[int]]) -> int:
        rows, cols = len(heights), len(heights[0])
        dirs = [(-1,0), (0,1), (0,-1), (1,0)]
        pq = [(0, 0, 0)]
        minSum = [[float("inf") for _ in range(cols)] for _ in range(rows)]
        minSum[0][0] = 0
        while pq:
            w, i, j = heappop(pq)
            for dx, dy in dirs:
                    x, y = i + dx, j + dy
                    if 0 <= x < rows and 0 <= y < cols and minSum[x][y] > max(w, abs(heights[x][y] - heights[i][j])):
                        minSum[x][y] = max(w, abs(heights[x][y] - heights[i][j]))
                        heappush(pq, (minSum[x][y], x, y))
        return minSum[rows-1][cols-1]

