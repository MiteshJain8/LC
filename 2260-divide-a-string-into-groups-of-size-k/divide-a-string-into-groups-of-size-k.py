class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        res = []
        n = len(s)
        i = 0
        while i < n - k:
            res.append(s[i:i+k])
            i += k
        if n % k != 0:
            times = n % k
            end = s[i:] + fill * (k - times)
            res.append(end)
        else:
            res.append(s[i:])
        return res