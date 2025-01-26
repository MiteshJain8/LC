class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        def dfs(i,j):
            if j == n-1:
                return triangle[j][i]
            if dp[j][i] != float(inf):
                return dp[j][i]

            # i
            left = triangle[j][i] + dfs(i, j+1)
            # i+1
            right = triangle[j][i] + dfs(i+1, j+1)
            dp[j][i] = min(left, right)
            return dp[j][i]

        n = len(triangle)
        dp = [[float(inf) for _ in range(i+1)] for i in range(n)]
        return dfs(0, 0)