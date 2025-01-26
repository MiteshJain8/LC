class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = [[triangle[j][i] for i in range(j+1)] for j in range(n)]
        for j in range(n-2, -1, -1):
            for i in range(j+1):
                dp[j][i] += min(dp[j+1][i], dp[j+1][i+1])
        return dp[0][0]