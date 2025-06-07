class Solution:
    def clearStars(self, s: str) -> str:
        res = list(s)
        n = len(s)
        pq = []
        for i in range(n):
            if s[i] == '*':
                ch, idx = heappop(pq)
                res[-idx] = ''
                res[i] = ''
            else:
                heappush(pq, (s[i], -i))
        return "".join(res)