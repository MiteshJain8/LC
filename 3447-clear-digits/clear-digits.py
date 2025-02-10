class Solution:
    def clearDigits(self, s: str) -> str:
        s = list(s)
        i, cnt = len(s)-1, 0
        while i > 0 :
            while s[i].isdigit():
                cnt += 1
                s[i] = ''
                i -= 1
            while cnt and not s[i].isdigit():
                cnt -= 1
                s[i] = ''
                i -= 1
            if not cnt and not s[i].isdigit():
                i -= 1
        return "".join(s)