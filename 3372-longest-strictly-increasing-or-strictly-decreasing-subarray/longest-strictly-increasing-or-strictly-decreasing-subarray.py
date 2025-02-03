class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        res, cur = 1, 1
        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                cur += 1
                res = max(res,cur)
            else:
                cur = 1
        cur = 1
        for i in range(1,len(nums)):
            if nums[i] < nums[i-1]:
                cur += 1
                res = max(res,cur)
            else:
                cur = 1
        return res