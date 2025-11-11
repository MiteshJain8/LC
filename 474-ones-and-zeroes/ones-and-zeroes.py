class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        def backtrack(i, zeroes, ones):
            if i >= l:
                return 0

            if dp[i][zeroes][ones] != -1:
                return dp[i][zeroes][ones]

            not_pick = backtrack(i+1, zeroes, ones)

            pick = 0
            z, o = hmap[i]
            if zeroes >= z and ones >= o: 
                pick = 1 + backtrack(i+1, zeroes - z, ones - o)

            dp[i][zeroes][ones] = max(pick, not_pick)
            return dp[i][zeroes][ones]

        l = len(strs)
        hmap = defaultdict(list)
        for i,s in enumerate(strs):
            z, o = 0, 0
            for c in s:
                if c == '1':
                    o += 1
                else:
                    z += 1
            hmap[i] = [z, o]
        dp = [[[-1 for _ in range(n+1)] for _ in range(m+1)] for _ in range(l)]
        return backtrack(0, m, n)