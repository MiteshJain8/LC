class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums.sort()
        res = []
        dp = [[num] for num in nums]
        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                if nums[j] % nums[i] == 0 and len(dp[j]) >= len(dp[i]):
                    dp[i] = [nums[i]] + dp[j]
            if len(dp[i]) > len(res):
                res = dp[i]
        return res