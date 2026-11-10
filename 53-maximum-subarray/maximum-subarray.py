class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        res, cur = float("-inf"), 0
        n = len(nums)
        for i in range(n):
            if cur < 0:
                cur = nums[i]
            else:
                cur += nums[i]
            res = max(res, cur)
        return res