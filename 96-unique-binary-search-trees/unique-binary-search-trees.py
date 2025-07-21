class Solution:
    def numTrees(self, n: int) -> int:
        def solve(k):
            if k <= 1:
                return 1

            if dp[k] != -1:
                return dp[k]

            res = 0
            for i in range(1, k+1):
                res += solve(i-1) * solve(k - i)

            dp[k] = res
            return res

        dp = [-1] * (n+1)
        return solve(n)