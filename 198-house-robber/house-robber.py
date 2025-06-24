class Solution:
    def rob(self, nums: List[int]) -> int:
        def  dfs(i):
            if i >= n:
                return 0
            if dp[i] != -1:
                return dp[i]

            dp[i] = dfs(i + 2) + nums[i]

            dp[i] = max(dfs(i + 1), dp[i])
            return dp[i]

        n = len(nums)
        dp = [-1] * n
        return dfs(0)