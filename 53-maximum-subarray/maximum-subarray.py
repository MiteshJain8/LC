class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = cur = float("-inf")
        for num in nums:
            if cur > 0:
                cur += num
            else:
                cur = max(cur, num)
            res = max(cur, res)

        return res