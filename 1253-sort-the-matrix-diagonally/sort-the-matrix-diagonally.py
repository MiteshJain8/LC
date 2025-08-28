class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        hmap = defaultdict(list)
        for i in range(m):
            for j in range(n):
                hmap[i-j].append(mat[i][j])

        for k in hmap.keys():
            hmap[k].sort(reverse=True)

        for i in range(m):
            for j in range(n):
                mat[i][j] = hmap[i-j].pop()

        return mat