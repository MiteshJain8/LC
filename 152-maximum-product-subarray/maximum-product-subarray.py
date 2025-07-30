class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cur_max = cur_min = 1
        res = max(nums)
        for num in nums:
            if not num:
                cur_max = cur_min = 1
                continue
            temp = cur_max * num
            cur_max = max(num, num * cur_max, num * cur_min)
            cur_min = min(num, temp, num * cur_min)
            res = max(res, cur_max)

        return res