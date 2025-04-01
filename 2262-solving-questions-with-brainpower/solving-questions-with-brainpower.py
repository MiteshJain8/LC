class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        def backtrack(i):
            if i >= n:
                return 0
            if dp[i] != -1:
                return dp[i]

            res1 = backtrack(i+1)
            res2 = backtrack(i+1+questions[i][1]) + questions[i][0]
            dp[i] = max(res1, res2)
            return dp[i]

        n = len(questions)
        dp = [-1] * n
        return backtrack(0)