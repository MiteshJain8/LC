class Solution {
public:
    vector<int> findMissingAndRepeatedValues(vector<vector<int>>& grid) {
        int n = grid.size();
        vector<bool> check(n*n+1, false);
        check[0] = true;
        vector<int> res(2);
        for (int i=0; i<n; i++) {
            for (int j=0; j<n; j++) {
                if (check[grid[i][j]])  res[0] = grid[i][j];
                check[grid[i][j]] = true;
            }
        }
        res[1] = find(check.begin(), check.end(), false) - check.begin();
        return res;
    }
};