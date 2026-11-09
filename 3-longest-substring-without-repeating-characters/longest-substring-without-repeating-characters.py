class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r, n = 0, 1, len(s)
        if n < 2:
            return n
        res, cur = 1, 1
        hset = set(s[0])
        while r < n:
            while s[r] in hset:
                hset.remove(s[l])
                l += 1
                cur -= 1
            hset.add(s[r])
            cur += 1
            res = max(cur, res)
            r += 1
        return res