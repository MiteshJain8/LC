class Solution:
    def minDistance(self, w1: str, w2: str) -> int:
        m, n = len(w1), len(w2)
        prev_dp = [i for i in range(n, -1, -1)]
        cur_dp = [0] * (n+1)
        for i in range(m-1, -1, -1):
            cur_dp[n] = m - i
            for j in range(n-1, -1, -1):
                if w1[i] == w2[j]:
                    cur_dp[j] = prev_dp[j+1]
                else:
                    cur_dp[j] = 1 + min(cur_dp[j+1], prev_dp[j], prev_dp[j+1])
            prev_dp = cur_dp
            cur_dp = [0] * (n+1)
        return prev_dp[0]