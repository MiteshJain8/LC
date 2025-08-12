class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = cur = float("-inf")
        for num in nums:
            cur = max(num, cur + num)
            res = max(cur, res)

        return res