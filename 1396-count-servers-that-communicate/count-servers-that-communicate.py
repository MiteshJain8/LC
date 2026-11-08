class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        rows, cols = defaultdict(int), defaultdict(int)
        r, c = len(grid), len(grid[0])
        res = 0
        for i in range(r):
            for j in range(c):
                if grid[i][j]:
                    rows[i] += 1
                    cols[j] += 1
        for i in range(r):
            for j in range(c):
                if grid[i][j]:
                    if rows[i] > 1 or cols[j] > 1:
                        res += 1
        return res
        
