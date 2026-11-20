class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        need, have, res, length = 0, 0, (0, 0), n+1
        tmap, smap = defaultdict(int), defaultdict(int)
        for c in t:
            if c not in tmap:
                need += 1
            tmap[c] += 1
        i, j = 0, 0
        while j <= n:
            if need == have:
                if s[i] in tmap:
                    smap[s[i]] -= 1
                    if smap[s[i]] < tmap[s[i]]:
                        have -= 1
                i += 1
            else:
                if j == n:
                    break
                if s[j] in tmap:
                    smap[s[j]] += 1
                    if smap[s[j]] == tmap[s[j]]:
                        have += 1
                j += 1
            if need == have and (j - i) < length:
                res = (i, j)
                length = j - i
        return s[res[0] : res[1]]
                