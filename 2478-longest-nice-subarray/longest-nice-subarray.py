class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        i = j = mask = res = 0
        while j < len(nums):
            if nums[j] & mask == 0:
                mask |= nums[j]
                res = max(res, j-i+1)
                j += 1
            else:
                while i < j and nums[j] & mask != 0:
                    mask ^= nums[i]
                    i += 1
        return res