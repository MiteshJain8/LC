class Solution:
    def climbStairs(self, n: int) -> int:
        nxt, cur, prev = 1, 1, 1
        for i in range(2, n+1):
            nxt = cur + prev
            prev = cur
            cur = nxt
        return cur