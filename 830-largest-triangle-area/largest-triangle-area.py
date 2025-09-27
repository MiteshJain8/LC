class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        area = 0.0
        for comb in combinations(points, 3):
            x1, x2, x3 = comb[0][0], comb[1][0], comb[2][0]
            y1, y2, y3 = comb[0][1], comb[1][1], comb[2][1]
            area = max(0.5*(abs(x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2))), area)

        return area