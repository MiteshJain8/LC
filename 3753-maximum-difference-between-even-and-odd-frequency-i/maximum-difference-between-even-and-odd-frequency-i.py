class Solution:
    def maxDifference(self, s: str) -> int:
        odd, eve = 1, 100
        hset = set()
        for c in s:
            if c in hset:
                continue
            hset.add(c)
            cnt = s.count(c)
            if cnt & 1:
                odd = max(odd, cnt)
            else:
                eve = min(eve, cnt)
        return odd-eve