class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        def backtrack(i, cur_or):
            if i == n:
                return 1 if cur_or == max_or else 0

            if dp[i][cur_or] != -1:
                return dp[i][cur_or]

            #leave
            leave = backtrack(i+1, cur_or)

            #take
            take = backtrack(i+1, cur_or | nums[i])

            dp[i][cur_or] = take + leave

            return dp[i][cur_or]

        n = len(nums)
        max_or = 0
        for num in nums:
            max_or |= num
        dp = [[-1 for _ in range(max_or+1)] for _ in range(n)]

        return backtrack(0, 0)