class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        def can_eat(k):
            t = 0
            for i in range(n):
                t += ceil(piles[i] / k)
                if t > h:
                    return False
            return True

        l, r = 1, max(piles)
        n = len(piles)
        res = r
        while l <= r:
            m = (r-l)//2 + l
            if can_eat(m):
                res = min(res, m)
                r = m-1
            else:
                l = m+1
        return res