class Solution:
    def sumZero(self, n: int) -> List[int]:
        if n == 1:
            return [0]

        res = [0] * n
        res[0] = -(((n-1) * n) // 2)
        for i in range(1, n):
            res[i] = i

        return res