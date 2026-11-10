class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        dp = [0] * (n+1)
        for i in range(n-1, -1, -1):
            #i+1
            dp[i] = costs[i] + 1 + dp[i+1]
            #i+2
            if i + 2 <= n:
                dp[i] = min(costs[i+1] + 4 + dp[i+2], dp[i])
            #i+3
            if i + 3 <= n:
                dp[i] = min(costs[i+2] + 9 + dp[i+3], dp[i])
        return dp[0]