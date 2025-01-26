class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        def dfs(i,j):
            if i < 0 or j < 0:
                return 0
            if obstacleGrid[i][j] == 1:
                return 0
            if i == 0 and j == 0:
                return 1
            if dp[i][j] != -1:
                return dp[i][j]

            left, up = 0, 0
            if i > 0:
                left = dfs(i-1, j)
            if j > 0:
                up = dfs(i, j-1)

            dp[i][j] = left + up
            return dp[i][j]

        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[-1 for _ in range(n)] for _ in range(m)]
        return dfs(m-1, n-1)