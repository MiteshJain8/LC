class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        tot = 3 * 2 ** (n-1)
        if k > tot:
            return ""
        res = []
        choices = "abc"
        left, right = 1, tot
        for _ in range(n):
            cur = left
            size = (right - left + 1) // len(choices)
            for c in choices:
                if cur <= k < cur + size:
                    res.append(c)
                    left = cur
                    right = cur + size - 1
                    choices = "abc".replace(c, '')
                    break
                cur += size
        return "".join(res)