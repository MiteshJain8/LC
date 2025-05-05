class Solution:
    def numTilings(self, n: int) -> int:
        dp_full = [0, 1, 2]
        dp_half = [0, 1, 2]
        modulo = 10 ** 9 + 7
        while len(dp_full) <= n:
            f = dp_full[-1] + dp_full[-2] + 2 * dp_half[-2]
            h = dp_full[-1] + dp_half[-1]
            dp_full.append(f % modulo)
            dp_half.append(h % modulo)
        
        return dp_full[n]