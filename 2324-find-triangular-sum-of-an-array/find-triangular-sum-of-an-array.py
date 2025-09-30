class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        n = len(nums) - 1
        while len(nums) > 1:
            newNums = [0] * (n)
            for i in range(n):
                newNums[i] = (nums[i] + nums[i+1]) % 10
            nums = newNums
            n -= 1

        return nums[0]