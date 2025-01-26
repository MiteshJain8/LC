class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] or obstacleGrid[-1][-1]:
            return 0
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [0 for _ in range(n)]
        dp[0] = 1
        for i in range(m):
            cur = [0 for _ in range(n)]
            for j in range(n):
                if obstacleGrid[i][j] != 1:
                    cur[j] = dp[j]
                    if j > 0:
                        cur[j] += cur[j-1]
            dp = cur
        return dp[n-1]