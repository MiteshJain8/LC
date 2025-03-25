class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        def count_cuts(coordinates):
            cnt = prev_end = 0
            for start, end in coordinates:
                if start >= prev_end:
                    cnt += 1
                prev_end = max(prev_end, end)
            return cnt

        r = len(rectangles)
        x_coordinates = [(rectangles[i][0], rectangles[i][2]) for i in range(r)]
        x_coordinates.sort()
        if count_cuts(x_coordinates) >= 3:
            return True
        y_coordinates = [(rectangles[i][1], rectangles[i][3]) for i in range(r)]
        y_coordinates.sort()
        if count_cuts(y_coordinates) >= 3:
            return True
        return False
