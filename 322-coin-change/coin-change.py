class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        def backtrack(remaining):
            if dp[remaining] != float("inf"):
                return dp[remaining]
            res = amount + 1
            for c in coins:
                if remaining - c < 0:
                    break
                res = min(res, backtrack(remaining - c) + 1)
            dp[remaining] = res
            return res

        dp = [float("inf")] * (amount+1)
        dp[0] = 0
        coins = list(set(coins))
        coins.sort()
        ans = backtrack(amount)
        return -1 if ans == amount + 1 else ans