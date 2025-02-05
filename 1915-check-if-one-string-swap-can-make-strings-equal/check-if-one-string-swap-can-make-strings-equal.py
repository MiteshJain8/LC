class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        c1, c2 = '', ''
        flag = 2
        for i in range(len(s1)-1):
            if s1[i] == s2[i]:
                continue
            if s1[i] != s2[i] and flag == 2:
                c1 = s1[i]
                c2 = s2[i]
                flag -= 1
            elif s1[i] != s2[i] and flag == 1:
                if s1[i] == c2 and s2[i] == c1:
                    flag -= 1
                else:
                    return False
            else:
                return False
        if flag == 1:
            return s1[-1] == c2 and s2[-1] == c1
        return s1[-1] == s2[-1]