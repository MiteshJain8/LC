class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        res, cur = nums[0], nums[0]
        n = len(nums)
        for i in range(1,n):
            if cur < 0:
                cur = nums[i]
            else:
                cur += nums[i]
            res = max(res, cur)
        return res