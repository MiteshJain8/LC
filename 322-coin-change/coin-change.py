class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        def backtrack(remaining):
            if not remaining:
                return 0

            if dp[remaining] != -1:
                return dp[remaining]

            res = float("inf")
            for c in coins:
                if remaining - c >= 0:
                    res = min(1 + backtrack(remaining - c), res)
            dp[remaining] = res
            return dp[remaining]
        
        coins.sort()
        dp = [-1] * (amount+1)
        res = backtrack(amount)
        return res if res != float("inf") else -1