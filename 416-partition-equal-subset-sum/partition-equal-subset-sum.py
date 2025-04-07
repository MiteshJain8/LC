class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        def bactrack(i, remain):
            if remain == 0:
                return True
            if remain < 0 or i >= n:
                return False
            if dp[i][remain] != -1:
                return dp[i][remain]

            res1 = bactrack(i+1, remain)
            res2 = bactrack(i+1, remain-nums[i])
            dp[i][remain] = res1 or res2
            return dp[i][remain]

        target = sum(nums)
        n = len(nums)
        if target & 1:
            return False
        target //= 2
        dp = [[-1 for _ in range(target+1)] for _ in range(n)]
        return bactrack(0, target)