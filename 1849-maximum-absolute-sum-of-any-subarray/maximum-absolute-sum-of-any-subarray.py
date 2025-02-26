class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        cur_sum = res = max_pre = min_pre = 0
        for num in nums:
            cur_sum += num
            res = max(abs(cur_sum-max_pre), abs(cur_sum-min_pre), res)
            max_pre = max(cur_sum, max_pre)
            min_pre = min(cur_sum, min_pre)
        return res