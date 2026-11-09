class Solution:
    def reverseBits(self, n: int) -> int:
        lst = [0] * 32
        b = bin(n)[2:][::-1]
        for i in range(len(b)):
            lst[i] = int(b[i])
        res = 0
        for e in lst:
            res *= 2
            res += e
        return res

