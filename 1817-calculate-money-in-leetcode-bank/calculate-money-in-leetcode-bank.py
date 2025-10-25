class Solution:
    def totalMoney(self, n: int) -> int:
        multiplier = n // 7
        full = 28 * multiplier + 7 * multiplier * (multiplier - 1) // 2
        extra = n % 7
        remainder = multiplier * extra + extra * (extra + 1) // 2
        return full + remainder