class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [questions[i][0] for i in range(n)]
        for i in range(n-2, -1, -1):
            j = i+1+questions[i][1]
            if j < n and dp[j] + questions[i][0] > dp[i+1]:
                dp[i] = dp[j] + questions[i][0]
            elif dp[i+1] > dp[i]:
                dp[i] = dp[i+1]
        return dp[0]