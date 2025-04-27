class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        i = res = 0
        for j in range(2, len(nums)):
            if (nums[i] + nums[j]) * 2 == nums[i+1]:
                res += 1
            i += 1
        return res