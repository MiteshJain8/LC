class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        res = 0
        for e in nums:
            res ^= e
        return res