class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        def backtrack(i, cur_sum):
            if cur_sum == n:
                return True
            if i < 0 or cur_sum > n:
                return False
            if backtrack(i-1, cur_sum + 3**i):
                return True
            return backtrack(i-1, cur_sum)

        return backtrack(floor(log(n,3)), 0)