class Solution:
    def countGoodNumbers(self, n: int) -> int:
        def power(x, n):
            res = 1
            while n > 0:
                if n & 1:
                    res = (res * x) % MOD
                n //= 2
                x = (x * x) % MOD
            return res

        MOD = 10 ** 9 + 7
        odd = n // 2
        even = n - odd
        return (power(5, even) * power(4, odd)) % MOD