class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        res = 0
        for i in range(low, high+1):
            s = str(i)
            l = len(s)
            if l & 1:
                continue
            if sum(int(j) for j in s[:l//2]) == sum(int(j) for j in s[l//2:]):
                res += 1
        return res