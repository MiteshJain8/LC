class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        op = set(['(', '[', '{'])
        hmap = {')': '(', ']': '[', '}': '{'}
        for c in s:
            if c in op:
                stack.append(c)
            elif stack and stack[-1] == hmap[c]:
                stack.pop()
            else:
                return False
        return False if stack else True