class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        eve_n = n // 2
        eve_m = m // 2
        return eve_m * (n - eve_n) + eve_n * (m - eve_m)