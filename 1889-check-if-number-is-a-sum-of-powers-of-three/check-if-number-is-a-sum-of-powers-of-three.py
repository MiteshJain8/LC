class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        def backtrack(i, cur_sum):
            if cur_sum == n:
                return True
            if i < 0 or cur_sum > n:
                return False

            select = backtrack(i-1, cur_sum + 3**i)
            ignore = backtrack(i-1, cur_sum)

            return select or ignore

        return backtrack(floor(log(n,3)), 0)