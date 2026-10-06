class Solution:
    def totalNQueens(self, n: int) -> int:
        def backtrack(r):
            if r >= n:
                return 1

            res = 0
            for c in range(n):
                if c in cols or r+c in rl_diag or r-c in lr_diag:
                    continue
                cols.add(c)
                rl_diag.add(r+c)
                lr_diag.add(r-c)

                res += backtrack(r+1)

                cols.remove(c)
                rl_diag.remove(r+c)
                lr_diag.remove(r-c)

            return res


        cols, lr_diag, rl_diag = set(), set(), set()
        return backtrack(0)