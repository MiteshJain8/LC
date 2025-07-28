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
                    print(s[i:j])
                    dp[i] = True
                    print(res[j], j)
                    for k in range(len(res[j])):
                        if res[j][k] == "":
                            val = s[i:j]
                        else:
                            val = s[i:j] + " " + res[j][k]
                        print(val, i, j)
                        res[i].append(val)
                        
            print(res[i])   
        return res[0]