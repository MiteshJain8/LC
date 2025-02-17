class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        def backtrack():
            res = 0
            for k,v in hmap.items():
                if v:
                    hmap[k] -= 1
                    res += backtrack() + 1
                    hmap[k] += 1
            return res

        hmap = Counter(tiles)
        return backtrack()
