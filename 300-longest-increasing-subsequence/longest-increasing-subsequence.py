class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res = [nums[0]]
        for val in nums:
            if res[-1] < val:
                res.append(val)
            else:
                idx = bisect.bisect_left(res, val)
                res[idx] = val

        return len(res)