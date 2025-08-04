class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n = len(fruits)
        hset = defaultdict(int)
        l = res = 0
        for r in range(n):
            hset[fruits[r]] += 1
            if len(hset) <= 2:
                res = max(res, r - l + 1)
            else:
                while len(hset) > 2:
                    hset[fruits[l]] -= 1
                    if hset[fruits[l]] == 0:
                        del hset[fruits[l]]
                    l += 1

        return res
