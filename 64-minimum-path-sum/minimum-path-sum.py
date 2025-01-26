class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        def dfs(i,j):
            if i == 0 and j == 0:
                return grid[0][0]

            if dp[i][j] != -1:
                return dp[i][j]

            # left
            left = float(inf)
            if i > 0:
                left = grid[i][j] + dfs(i-1, j)
            # up
            up = float(inf)
            if j > 0:
                up = grid[i][j] + dfs(i, j-1)

            dp[i][j] = min(left, up)
            return dp[i][j]

        m, n = len(grid), len(grid[0])
        dp = [[-1 for _ in range(n)] for _ in range(m)]
        return dfs(m-1,n-1)