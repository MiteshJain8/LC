class Solution:
    def climbStairs(self, n: int) -> int:
        zero, one, two = 1, 1, 2
        for i in range(1,n):
            two = zero + one
            zero, one = one, two
        return one