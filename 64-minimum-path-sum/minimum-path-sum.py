class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        cur_dp = [0] * (n+1)
        prev_dp = [0] * (n+1)
        for j in range(n-1, -1, -1):
            prev_dp[j] = grid[m-1][j] + prev_dp[j+1]
        for i in range(m-2, -1, -1):
            cur_dp[n-1] = grid[i][n-1] + prev_dp[n-1]
            for j in range(n-2, -1, -1):
                cur_dp[j] = grid[i][j] + min(cur_dp[j+1], prev_dp[j])
            prev_dp = cur_dp
                
        return prev_dp[0]