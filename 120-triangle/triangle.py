class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for j in range(len(triangle)-2, -1, -1):
            for i in range(j+1):
                triangle[j][i] += min(triangle[j+1][i], triangle[j+1][i+1])
        return triangle[0][0]