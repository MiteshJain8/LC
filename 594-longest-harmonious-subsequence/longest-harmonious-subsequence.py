class Solution:
    def findLHS(self, nums: List[int]) -> int:
        hmap = Counter(nums)
        res = 0
        hmap = dict(sorted(hmap.items()))
        for k,v in hmap.items():
            if k-1 in hmap:
                res = max(res, v + hmap[k-1])

        return res