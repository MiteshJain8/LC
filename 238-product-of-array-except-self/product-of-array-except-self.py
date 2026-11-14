class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        zero_cnt = 0
        prod = 1
        for e in nums:
            if e:
                prod *= e
            else:
                zero_cnt += 1
                if zero_cnt > 1:
                    return [0] * len(nums)
        return [0 if e else prod for e in nums] if zero_cnt else [prod // e for e in nums]