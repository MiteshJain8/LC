class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        p = 0
        n = len(nums)
        res = [True] * n
        for i in range(n):
            p = ((p << 1) + nums[i]) % 5
            res[i] = p == 0

        return res