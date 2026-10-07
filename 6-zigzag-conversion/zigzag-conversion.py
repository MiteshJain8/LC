class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        lst = [[] for _ in range(numRows)]
        n = len(s)
        i, j = 0, 0
        asc = True
        while j < n:
            lst[i].append(s[j])
            j += 1
            if asc:
                i = (i + 1) % numRows
                if i == 0:
                    asc = False
                    i = numRows - 2
            else:
                i -= 1
                if i == -1:
                    asc = True
                    i = 1
        res = ""
        for k in range(numRows):
            cur = "".join(lst[k])
            res += cur
        return res