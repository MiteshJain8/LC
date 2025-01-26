class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[0][0] = grid[0][0]
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                up = float(inf)
                if i > 0:
                    up = grid[i][j] + dp[i-1][j]
                left = float(inf)
                if j > 0:
                    left = grid[i][j] + dp[i][j-1]
                dp[i][j] = min(left, up)
        return dp[m-1][n-1]