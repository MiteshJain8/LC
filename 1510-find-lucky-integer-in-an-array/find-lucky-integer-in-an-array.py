class Solution:
    def findLucky(self, arr: List[int]) -> int:
        hmap = Counter(arr)
        hmap = sorted(hmap.items(), reverse=True)
        for k,v in hmap:
            if k == v:
                return k

        return -1