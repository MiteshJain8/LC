class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        res = maxi = max_diff = 0
        for num in nums:
            res = max(res, max_diff * num)
            max_diff = max(max_diff, maxi - num)
            maxi = max(maxi, num)
        return res