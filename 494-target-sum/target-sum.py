class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        def backtrack(curSum, idx):
            if idx == n:
                return 1 if curSum == target else 0
            if (curSum, idx) in dp:
                return dp[(curSum, idx)]
            # add
            res = backtrack(curSum + nums[idx], idx + 1)
            # sub
            res += backtrack(curSum - nums[idx], idx + 1)
            dp[(curSum, idx)] = res
            return res

        n = len(nums)
        dp = {}
        return backtrack(0, 0)
