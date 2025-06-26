class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        power = 1
        res = 0
        for val in s[::-1]:
            if val == '0':
                res += 1
            elif val == '1' and power <= k:
                k -= power
                res += 1
            if power <= k:
                power *= 2

        return res