class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:
        MOD = 10**9 + 7
        max_len = min(n, 14)
        factorial = [1] * (n + 1)
        inv_fact = [1] * (n + 1)
        for i in range(1, n + 1): factorial[i] = factorial[i - 1] * i % MOD
        inv_fact[n] = pow(factorial[n], MOD - 2, MOD)
        for i in range(n - 1, -1, -1): inv_fact[i] = inv_fact[i + 1] * (i + 1) % MOD
        def C(a, b): return 0 if b > a or b < 0 else factorial[a] * inv_fact[b] % MOD * inv_fact[a - b] % MOD
        dp = [defaultdict(int) for _ in range(max_len + 1)]
        for i in range(1, maxValue + 1): dp[1][i] = 1
        for length in range(2, max_len + 1):
            for v in dp[length - 1]:
                for mul in range(2, (maxValue // v) + 1):
                    dp[length][v * mul] = (dp[length][v * mul] + dp[length - 1][v]) % MOD
        ans = 0
        for length in range(1, max_len + 1):
            total = sum(dp[length].values())
            ans = (ans + total * C(n - 1, length - 1)) % MOD
        return ans