class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        hmap = defaultdict(int)
        hset = []
        for x in range(n):
            for y in range(n):
                if img1[x][y]:
                    hset.append((x,y))
        for x in range(n):
            for y in range(n):
                if img2[x][y]:
                    for a,b in hset:
                        dx, dy = x-a, y-b
                        hmap[(dx, dy)] += 1
        lst = list(hmap.values())
        return max(lst)if lst else 0