class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        hlist = [0] * (m*n + 1)
        for i in range(m):
            for j in range(n):
                hlist[mat[i][j]] = (i, j)
        rows = [0] * m
        cols = [0] * n
        for i in range(m*n):
            r, c = hlist[arr[i]]
            if rows[r] == n-1:
                return i
            rows[r] += 1
            if cols[c] == m-1:
                return i
            cols[c] += 1
        