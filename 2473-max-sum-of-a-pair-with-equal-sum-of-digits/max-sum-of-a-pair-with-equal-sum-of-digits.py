class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        prefix = [0] * 82
        n, res = len(nums), -1
        for i in range(n):
            num = nums[i]
            dig = 0
            while num:
                dig += num % 10
                num //= 10
            if prefix[dig]:
                res = max(res, nums[i]+prefix[dig])
                prefix[dig] = max(nums[i], prefix[dig])
            else:
                prefix[dig] = nums[i]
        return res