class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        bot, top = 0, sum(grid[0]) - grid[0][0]
        maxx = top
        for i in range(1, len(grid[0])):
            top -= grid[0][i]
            bot += grid[1][i-1]
            maxx = min(maxx, max(bot, top))
        return maxx