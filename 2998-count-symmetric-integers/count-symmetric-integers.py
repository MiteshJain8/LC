class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        res = 0
        for i in range(low, high+1):
            s = str(i)
            l = len(s)
            if l & 1:
                continue
            sum1 = sum(int(s[j]) for j in range(l//2))
            sum2 = sum(int(s[j]) for j in range(l//2, l))
            if sum1 == sum2:
                res += 1
        return res