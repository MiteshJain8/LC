class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        def backtrack(rem, i):
            if i ** x == rem:
                return 1
            if i ** x > rem:
                return 0

            if dp[rem][i] != -1:
                return dp[rem][i]

            res = backtrack(rem, i+1) % mod
            res += backtrack(rem - i ** x, i+1) % mod

            dp[rem][i] = res

            return res

        mod = 10 ** 9 + 7
        dp = [[-1] * (n+1) for _ in range(n+1)]
        return backtrack(n, 1) % mod