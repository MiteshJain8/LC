class Solution:
    def climbStairs(self, n: int) -> int:
        def backtrack(k):
            if k < 0:
                return 0
            if k == 0:
                return 1
            if dp[k] != -1:
                return dp[k]
            dp[k] = backtrack(k-1) + backtrack(k-2)
            return dp[k]

        dp = [-1] * (n+1)
        dp[0], dp[1] = 1, 1
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]