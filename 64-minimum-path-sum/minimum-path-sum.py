class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[0] * (n+1) for _ in range(m+1)]
        for j in range(n-1, -1, -1):
            dp[m-1][j] = grid[m-1][j] + dp[m-1][j+1]
        for i in range(m-2, -1, -1):
            dp[i][n-1] = grid[i][n-1] + dp[i+1][n-1]
            for j in range(n-2, -1, -1):
                dp[i][j] = grid[i][j] + min(dp[i][j+1], dp[i+1][j])

        return dp[0][0]