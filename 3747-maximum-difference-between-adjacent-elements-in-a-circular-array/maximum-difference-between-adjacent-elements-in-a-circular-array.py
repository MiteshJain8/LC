class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        prev = nums[-1]
        res = 0
        for cur in nums:
            res = max(res, abs(cur - prev))
            prev = cur
        return res