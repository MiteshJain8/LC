class Solution:
    def findLHS(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        n = len(nums)
        i = j = 0
        while j < n:
            if nums[j] == nums[i]:
                j += 1
            elif nums[j] - nums[i] == 1:
                res = max(res, j-i+1)
                j += 1
            else:
                i += 1

        return res