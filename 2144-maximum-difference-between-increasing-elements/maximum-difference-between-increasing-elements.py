class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        n = len(nums)
        res = -1
        prev = nums[0]
        for i in range(1,n):
            if nums[i] > prev:
                res = max(res, nums[i]-prev)
            else:
                prev = nums[i]
        return res