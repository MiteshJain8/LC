class Solution:
    def climbStairs(self, n: int) -> int:
        def dfs(i):
            if i <= 1:
                return 1
            if dp[i]:
                return dp[i]

            dp[i] = dfs(i - 1) + dfs(i - 2)
            return dp[i]

        dp = [0] * (n+1)
        return dfs(n)