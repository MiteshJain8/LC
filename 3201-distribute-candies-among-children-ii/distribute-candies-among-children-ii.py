class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        if n > 3 * limit: return 0
        child1_min = max(0, n - 2 * limit)
        child1_max = min(n, limit)
        res = 0
        for i in range(child1_min, child1_max+1):
            m = n - i
            child2_min = max(0, m - limit)
            child2_max = min(m, limit)
            res += (child2_max - child2_min + 1)
        return res