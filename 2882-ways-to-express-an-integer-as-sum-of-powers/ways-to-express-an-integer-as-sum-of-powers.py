class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        @cache
        def backtrack(rem, i):
            if i ** x == rem:
                return 1
            if i ** x > rem:
                return 0

            res = backtrack(rem, i+1) % mod
            res += backtrack(rem - i ** x, i+1) % mod

            return res

        mod = 10 ** 9 + 7
        return backtrack(n, 1) % mod