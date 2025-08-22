class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        t, b, l, r = m-1, 0, n-1, 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    t = min(t, i)
                    b = max(b, i)
                    l = min(l, j)
                    r = max(r, j)
        return (b-t+1) * (r-l+1)