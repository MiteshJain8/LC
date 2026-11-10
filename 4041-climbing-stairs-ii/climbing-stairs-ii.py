class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        dp = [0] * (n+1)
        cur, nxt1, nxt2, nxt3 = 0, 0, 0, 0
        for i in range(n-1, -1, -1):
            #i+1
            cur = costs[i] + 1 + nxt1
            #i+2
            if i + 2 <= n:
                cur = min(costs[i+1] + 4 + nxt2, cur)
            #i+3
            if i + 3 <= n:
                cur = min(costs[i+2] + 9 + nxt3, cur)
            nxt3 = nxt2
            nxt2 = nxt1
            nxt1 = cur
        return cur