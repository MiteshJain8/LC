class Solution:
    def hasSameDigits(self, s: str) -> bool:
        n = len(s)
        nums = list(s)
        nums = list(map(int, s))
        for i in range(n-2):
            for j in range(n-i-1):
                nums[j] = (nums[j] + nums[j+1]) % 10
        print(nums)
        return nums[0] == nums[1]