class Solution:
    def countSquares(self, mat: List[List[int]]) -> int:
        rows, cols = len(mat), len(mat[0])
        res = 0
        dp = [0] * cols
        for r in range(rows):
            cur_dp = [0] * cols
            for c in range(cols):
                if mat[r][c]:
                    cur_dp[c] = 1 + min(
                        cur_dp[c-1], dp[c-1], dp[c]
                    )
                    res += cur_dp[c]
            dp = cur_dp
        return res