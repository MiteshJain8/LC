class Solution:
    def jump(self, nums: list[int]) -> int:
        n = len(nums)
        dp = [0] * n
        idx = 1
        for i in range(n-1):
            j = i + nums[i]
            if j >= idx:
                while idx < n and idx <= j:
                    dp[idx] = dp[i] + 1
                    idx += 1
            if idx >= n:
                break
        return dp[n-1]