class Solution:
    def convert(self, s: str, numRows: int) -> str:
        keep = [[] for _ in range(numRows)]
        i = 0
        flag = True
        for j in range(len(s)):
            keep[i].append(s[j])
            if flag:
                if i < numRows - 1:
                    i += 1
                else:
                    flag = False
                    i -= 1
            else:
                if i > 0:
                    i -= 1
                else:
                    flag = True
                    i += 1
        res = ""
        for lst in keep:
            res += "".join(lst)
        # print(keep)
        return res