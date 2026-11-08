class Solution:
    def rob(self, nums: list[int]) -> int:
        def backtrack(k):
            if k > n-1:
                return 0
            if dp[k] != -1:
                return dp[k]
            #rob
            res = nums[k] + backtrack(k+2)
            #no rob
            dp[k] = max(res, backtrack(k+1))
            return dp[k]

        n = len(nums)
        dp = [-1] * n
        return backtrack(0)