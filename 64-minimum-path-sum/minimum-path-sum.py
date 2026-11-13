class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [0] * n
        dp[0] = grid[0][0]
        for j in range(1, n):
            dp[j] = dp[j-1] + grid[0][j]
        for i in range(1, m):
            tmp = [0] * n
            tmp[0] = dp[0] + grid[i][0]
            for j in range(1, n):
                tmp[j] = min(dp[j], tmp[j-1]) + grid[i][j]
            dp = tmp
        return dp[n-1]

