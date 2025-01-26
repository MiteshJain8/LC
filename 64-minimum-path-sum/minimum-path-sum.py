class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [0 for _ in range(n)]
        for i in range(m):
            cur = [float(inf) for _ in range(n)]
            if i == 0:
                cur[0] = grid[0][0]
            for j in range(n):
                if i > 0:
                    cur[j] = grid[i][j] + dp[j]
                if j > 0:
                    cur[j] = min(cur[j], grid[i][j] + cur[j-1])
            dp = cur
        return dp[n-1]