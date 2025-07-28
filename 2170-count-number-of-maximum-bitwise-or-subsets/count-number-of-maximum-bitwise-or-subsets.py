class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        def backtrack(i, cur_or):
            if i == n:
                return 1 if cur_or == max_or else 0

            #leave
            leave = backtrack(i+1, cur_or)

            #take
            take = backtrack(i+1, cur_or | nums[i])

            return take + leave

        n = len(nums)
        max_or = 0
        for num in nums:
            max_or |= num

        return backtrack(0, 0)