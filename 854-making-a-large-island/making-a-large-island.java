class Solution {
    public int largestIsland(int[][] grid) {
        int n = grid.length;
        int res = 0;
        List<int[]> hlist = new ArrayList<>();
        Map<Integer, Integer> hmap = new HashMap<>();
        int[][] dirs = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
        
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                if (grid[i][j] == 1) {
                    res++;
                    int area = dfs(grid, i, j, res + 1, dirs);
                    hmap.put(res + 1, area);
                } else if (grid[i][j] == 0) {
                    hlist.add(new int[]{i, j});
                }
            }
        }

        if (res == 0) {
            return 1;
        }
        if (hmap.get(2) == n * n) {
            return n * n;
        }

        res = 1;
        for (int[] p : hlist) {
            int i = p[0], j = p[1];
            int cnt = 1;
            Set<Integer> cntset = new HashSet<>();
            cntset.add(0);
            for (int[] dir : dirs) {
                int x = i + dir[0];
                int y = j + dir[1];
                if (x >= 0 && x < n && y >= 0 && y < n && !cntset.contains(grid[x][y])) {
                    cnt += hmap.getOrDefault(grid[x][y], 0);
                    cntset.add(grid[x][y]);
                }
            }
            res = Math.max(res, cnt);
        }

        return res;
    }

    private int dfs(int[][] grid, int i, int j, int label, int[][] dirs) {
        int n = grid.length;
        int cnt = 1;
        grid[i][j] = label;
        for (int[] dir : dirs) {
            int x = i + dir[0];
            int y = j + dir[1];
            if (x >= 0 && x < n && y >= 0 && y < n && grid[x][y] == 1) {
                cnt += dfs(grid, x, y, label, dirs);
            }
        }
        return cnt;
    }
}