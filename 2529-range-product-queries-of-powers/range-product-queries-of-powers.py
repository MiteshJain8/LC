class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        i = 1
        mod = 1e9 + 7
        pows = []
        while i <= n:
            if n & i:
                pows.append(i)
            i <<= 1
        q = len(queries)
        res = [1] * q
        for j in range(q):
            start = queries[j][0]
            end = queries[j][1]
            for k in range(start, end+1):
                res[j] = (res[j] * pows[k]) % mod
            res[j] = int(res[j])

        return res