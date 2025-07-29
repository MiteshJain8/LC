class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def backtrack(remaining):
            if dp[remaining] != float("inf"):
                return dp[remaining]

            res = amount + 1
            for c in coins:
                if remaining - c < 0:
                    break
                res = min(res, 1 + backtrack(remaining - c))

            dp[remaining] = res
            return res

        dp = [float("inf")] * (amount + 1)
        dp[0] = 0
        coins.sort()
        ans = backtrack(amount)
        return -1 if ans == amount + 1 else ans