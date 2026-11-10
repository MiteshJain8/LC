class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        def backtrack(i):
            if i == n:
                return 0
            if dp[i] != -1:
                return dp[i]
            #i+1
            res = costs[i] + 1 + backtrack(i+1)
            #i+2
            if i + 2 <= n:
                res = min(costs[i+1] + 4 + backtrack(i+2), res)
            #i+3
            if i + 3 <= n:
                res = min(costs[i+2] + 9 + backtrack(i+3), res)
            dp[i] = res
            return res

        dp = [-1] * n
        return backtrack(0)