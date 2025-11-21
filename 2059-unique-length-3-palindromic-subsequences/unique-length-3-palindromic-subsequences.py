class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        left, right, res = set(), Counter(s), set()
        for m in s:
            right[m] -= 1
            for c in left:
                if right[c] > 0:
                    res.add((c,m))
            left.add(m)
        return len(res)