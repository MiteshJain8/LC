class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        w1, w2 = len(word1), len(word2)
        prev_dp = [w2 - i for i in range(w2+1)]
        cur_dp = [0] * (w2 + 1)
        for i in range(w1-1, -1, -1):
            cur_dp[w2] = w1 - i
            for j in range(w2-1, -1, -1):
                if word2[j] == word1[i]:
                    cur_dp[j] = prev_dp[j+1]
                else:
                    cur_dp[j] = 1 + min(cur_dp[j+1], prev_dp[j], prev_dp[j+1])
            prev_dp = cur_dp
            cur_dp = [0] * (w2 + 1)
        return prev_dp[0]