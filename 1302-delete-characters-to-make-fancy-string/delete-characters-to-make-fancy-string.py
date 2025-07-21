class Solution:
    def makeFancyString(self, s: str) -> str:
        if len(s) < 3:
            return s

        lst = list(s)
        for i in range(2, len(s)):
            if lst[i] == lst[i-1] and lst[i] == lst[i-2]:
                lst[i-2] = ''

        return "".join(lst)