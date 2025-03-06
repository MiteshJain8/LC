class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        check = [False] * (n*n+1)
        check[0] = True
        res = [0, 0]
        for i in range(n):
            for j in range(n):
                if check[grid[i][j]]:
                    res[0] = grid[i][j]
                check[grid[i][j]] = True
        res[1] = check.index(False)
        return res