class Solution:
    def clearDigits(self, s: str) -> str:
        s, hset = list(s), set(['0','1','2','3','4','5','6','7','8','9'])
        i, cnt = len(s)-1, 0
        while i > 0 :
            while s[i] in hset:
                cnt += 1
                s[i] = ''
                i -= 1
            while cnt and s[i] not in hset:
                cnt -= 1
                s[i] = ''
                i -= 1
            if not cnt and s[i] not in hset:
                i -= 1
        return "".join(s)