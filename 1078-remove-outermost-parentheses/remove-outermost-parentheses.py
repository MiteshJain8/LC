class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        lst = []
        n, j = len(s), 0
        op, cl = 0, 0
        for i in range(n):
            if s[i] == '(':
                op += 1
            else:
                cl += 1
            if op == cl:
                lst.append(s[j+1 : i])
                j = i+1
        return "".join(lst)