class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        l = 0
        res = cur = blocks[:k].count('W')
        for r in range(k,len(blocks)):
            if blocks[r] == 'W':
                cur += 1
            if blocks[l] == 'W':
                cur -= 1
                res = min(res, cur)
            l += 1
        return res