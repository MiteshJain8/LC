class Solution {
    public int[] findMissingAndRepeatedValues(int[][] grid) {
        int n = grid.length;
        boolean[] check = new boolean[n*n+1];
        check[0] = true;
        int[] res = new int[2];
        for (int i=0; i<n; i++) {
            for (int j=0; j<n; j++) {
                if (check[grid[i][j]] == true)  res[0] = grid[i][j];
                check[grid[i][j]] = true;
            }
        }
        for (int i = 0; i < n*n+1; i++) {
            if (check[i] == false) {
                res[1] = i;
                break;
            }
        }
        return res;
    }
}