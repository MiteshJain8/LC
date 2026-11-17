class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        t1, t2 = len(text1), len(text2)
        prev_dp, cur_dp = [0] * (t2+1), [0] * (t2+1)
        for i in range(t1-1, -1, -1):
            for j in range(t2-1, -1, -1):
                if text1[i] == text2[j]:
                    cur_dp[j] = prev_dp[j+1] + 1
                else:
                    cur_dp[j] = max(cur_dp[j+1], prev_dp[j])
            prev_dp = cur_dp
            cur_dp = [0] * (t2+1)
        return prev_dp[0]