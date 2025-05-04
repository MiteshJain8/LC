class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        hmap = defaultdict(int)
        res = 0
        for a,b in dominoes:
            if (a,b) in hmap:
                res += hmap[(a,b)]
            if a != b and (b,a) in hmap:
                res += hmap[(b,a)]
            hmap[(a,b)] += 1
        return res