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
        return backtrack(n)