class Solution:
    def minInsertions(self, s: str) -> int:
        o, ans, i, n = 0, 0, 0, len(s)

        while i < n:

            if s[i] == "(":
                o += 1
                i += 1
            else:
                if i + 1 < n and s[i + 1] == ")":
                    i += 2
                else:
                    ans += 1
                    i += 1

                if o > 0:
                    o -= 1
                else:
                    ans += 1

        ans += 2 * o

        return ans