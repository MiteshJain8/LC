class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        hmap = defaultdict(list)
        n = len(grid)
        for i in range(n):
            for j in range(n):
                hmap[i-j].append(grid[i][j])

        for k in hmap.keys():
            if k < 0:
                hmap[k].sort(reverse=True)
            else:
                hmap[k].sort()

        for i in range(n):
            for j in range(n):
                grid[i][j] = hmap[i-j].pop()

        return grid