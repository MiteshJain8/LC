class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        def backtrack(remaining):
            if not remaining:
                return 0
            if dp[remaining]:
                return dp[remaining]
            res = float("inf")
            for c in coins:
                if remaining - c >= 0:
                    res = min(res, 1 + backtrack(remaining - c))
                else:
                    break
            dp[remaining] = res
            return res

        dp = [0] * (amount + 1)
        coins.sort()
        ans = backtrack(amount)
        return -1 if ans == float("inf") else ans