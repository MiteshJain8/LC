class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        i = neg = pos = 0
        n = len(nums)
        while i < n and nums[i] < 0:
            i += 1
            neg += 1
        while i < n and nums[i] == 0:
            i += 1
        while i < n and nums[i] > 0:
            i += 1
            pos += 1
        return max(neg, pos)