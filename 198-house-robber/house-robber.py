class Solution:
    def rob(self, nums: List[int]) -> int:
        def dfs(i):
            # end
            if i >= n:
                return 0
            if i == n-1:
                return nums[i]
            if dp[i] != -1:
                return dp[i]
            # rob
            rob = nums[i] + dfs(i+2)
            # no rob
            no_rob = dfs(i+1)

            dp[i] = max(rob, no_rob)
            return dp[i]

        n = len(nums)
        dp = [-1] * n
        return dfs(0)