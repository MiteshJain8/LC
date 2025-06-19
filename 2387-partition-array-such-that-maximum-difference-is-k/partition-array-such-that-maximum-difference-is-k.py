class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums = list(set(nums))
        nums.sort()
        n = len(nums)
        i = j = 0
        res = 0
        while i < n:
            j = bisect_left(nums, nums[i] + k, i)
            i = j + (0 if j < n and nums[j] - nums[i] > k else 1)
            res += 1
        return res