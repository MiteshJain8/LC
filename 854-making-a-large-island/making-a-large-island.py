class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        def dfs(i,j, label):
            grid[i][j] = label
            cnt = 1
            for dx, dy in dirs:
                x, y = i+dx, j+dy
                if 0 <= x < n and 0 <= y < n and grid[x][y] == 1:
                    cnt += dfs(x,y,label)
            return cnt

        n, res = len(grid), 0
        hlist, hmap = [], defaultdict(int)
        dirs = [(0,1), (1,0), (0,-1), (-1,0)]
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    res += 1
                    area = dfs(i,j,res+1)
                    hmap[res+1] = area
                elif not grid[i][j]:
                    hlist.append((i,j))
        if not res:
            return 1
        if hmap[2] == n*n:
            return n*n
        res = 1
        for i,j in hlist:
            cnt, cntset = 1, set([0])
            for dx,dy in dirs:
                x, y = i+dx, j+dy
                if 0 <= x < n and 0 <= y < n and grid[x][y] not in cntset:
                    cnt += hmap[grid[x][y]]
                    cntset.add(grid[x][y])
            res = max(res, cnt)
        return res