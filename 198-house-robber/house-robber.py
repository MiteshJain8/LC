class Solution:
    def rob(self, nums: list[int]) -> int:
        n = len(nums)
        dp = [-1] * (n+1)
        dp[-1] = 0
        dp[n-1] = nums[-1]
        for i in range(n-2, -1, -1):
            dp[i] = max(dp[i+1], nums[i] + dp[i+2])
        return dp[0]