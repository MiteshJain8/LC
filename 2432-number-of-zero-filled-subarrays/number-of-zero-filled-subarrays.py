class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        res = 0
        l = -1
        for r in range(len(nums)):
            if nums[r] == 0:
                res += (r - l)
            else:
                l = r

        return res