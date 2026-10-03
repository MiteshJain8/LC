class Solution:
    def longestValidParentheses(self, s: str) -> int:
        op, cl, res = 0, 0, 0
        for c in s:
            if c == '(':
                op += 1
            else:
                cl += 1
            if cl > op:
                op, cl = 0, 0
            elif cl == op:
                res = max(res, op + cl)
        op, cl = 0, 0
        for c in reversed(s):
            if c == ')':
                op += 1
            else:
                cl += 1
            if cl > op:
                op, cl = 0, 0
            elif cl == op:
                res = max(res, op + cl)

        return res