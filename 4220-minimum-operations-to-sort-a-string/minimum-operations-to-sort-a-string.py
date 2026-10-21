class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)

        if all(s[i] <= s[i + 1] for i in range(n - 1)):
            return 0
        if n == 2:
            return -1

        mn_char, mx_char = min(s), max(s)

        if s[0] == mn_char or s[-1] == mx_char:
            return 1

        if (mn_char in s[1:-1]) or (mx_char in s[1:-1]):
            return 2
        return 3