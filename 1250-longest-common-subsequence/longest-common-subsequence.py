class Solution:
    def longestCommonSubsequence(self, t1: str, t2: str) -> int:
        m, n = len(t1), len(t2)
        prev_dp = [0] * (n+1)
        cur_dp = [0] * (n+1)
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if t1[i] == t2[j]:
                    cur_dp[j] = 1 + prev_dp[j+1]
                else:
                    cur_dp[j] = max(prev_dp[j], cur_dp[j+1])
            prev_dp = cur_dp
            cur_dp = [0] * (n+1)
        return prev_dp[0]
