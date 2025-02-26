class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        cur_max_sum, max_sum = nums[0], nums[0]
        cur_min_sum, min_sum = nums[0], nums[0]
        for i in range(1,len(nums)):
            cur_max_sum = max(nums[i], nums[i]+cur_max_sum)
            cur_min_sum = min(nums[i], nums[i]+cur_min_sum)
            max_sum = max(max_sum, cur_max_sum)
            min_sum = min(min_sum, cur_min_sum)
        return max(max_sum, abs(min_sum))