class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        i = 1
        mod = 1e9 + 7
        pows = []
        while i <= n:
            if n & i:
                pows.append(i)
            i <<= 1
        res = []
        for start, end in queries:
            prod = 1
            for k in range(start, end+1):
                prod = prod * pows[k] % mod
            res.append(int(prod))

        return res