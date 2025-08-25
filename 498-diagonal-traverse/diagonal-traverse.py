class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        res = []
        m, n = len(mat), len(mat[0])
        hmap = defaultdict(list)
        for i in range(m):
            for j in range(n):
                hmap[i+j].append(mat[i][j])
        for k,v in hmap.items():
            if k & 1:
                res.extend(v)
            else:
                res.extend(v[::-1])

        return res