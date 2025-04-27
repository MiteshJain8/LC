class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        res = 0
        for j in range(2, len(nums)):
            if (nums[j-2] + nums[j]) * 2 == nums[j-1]:
                res += 1
        return res