class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        res = [""] * ceil(len(s) / k)
        i = 0
        for j in range(len(res)):
            res[j] = s[i:i+k]
            i += k

        res[-1] += fill * (k - len(res[-1]))
        return res