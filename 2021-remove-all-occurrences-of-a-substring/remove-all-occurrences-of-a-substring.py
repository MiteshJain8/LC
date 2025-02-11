class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = []
        n, m = len(s), len(part)
        i = 0
        for i in range(n):
            stack.append(s[i])
            p = len(stack)
            if p >= m and stack[-1] == part[-1]:
                for j in range(1,m):
                    if stack[p-1-j] != part[-1-j]:
                        break
                else:
                    stack = stack[:-m] 
        return "".join(stack)