class Solution:
    def maxOperations(self, s: str) -> int:
        one_cnt = res = i = 0
        n = len(s)
        while i < n:
            if s[i] == '1':
                one_cnt += 1
                i += 1
            else:
                while i < n and s[i] == '0':
                    i += 1
                res += one_cnt
        return res