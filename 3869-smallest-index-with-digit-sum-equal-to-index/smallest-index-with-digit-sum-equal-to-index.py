class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        def calc_sum(num):
            sm = 0
            while num:
                sm += num % 10
                num = num // 10
            return sm

        for i in range(len(nums)):
            if i == calc_sum(nums[i]):
                return i

        return -1