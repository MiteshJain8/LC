class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        hset = set(wordDict)
        n = len(s)
        dp = [False] * (n+1)
        res = [[] for _ in range(n+1)]
        dp[n] = True
        res[n].append("")
        for i in range(n-1, -1, -1):
            for j in range(i+1, n+1):
                if dp[j] and s[i:j] in hset:
                    dp[i] = True
                    for k in range(len(res[j])):
                        if res[j][k] == "":
                            val = s[i:j]
                        else:
                            val = s[i:j] + " " + res[j][k]
                        res[i].append(val)
                        
        return res[0]