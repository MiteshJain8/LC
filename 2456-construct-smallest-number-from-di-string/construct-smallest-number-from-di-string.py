class Solution:
    def smallestNumber(self, pattern: str) -> str:
        n = len(pattern)
        res = [''] * (n+1)
        i, cnt, cur = 0, 1, 1
        while i <= n:
            j = i
            while j < n and pattern[j] == 'D':
                cnt += 1
                j += 1
            cur = cnt + 1
            while i <= j:
                res[i] = str(cnt)
                cnt -= 1
                i += 1
            cnt = cur
        return "".join(res)
            
            