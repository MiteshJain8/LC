class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        points.sort(key=lambda p: (p[0], -p[1]))
        cnt = 0
        for i in range(len(points)):
            x0, y0 = points[i]
            bot, top = float("-inf"), y0
            for j in range(i + 1, len(points)):
                x1, y1 = points[j]
                if y1 <= top and y1 > bot:
                    cnt += 1
                    bot = y1
                    if y1 == top:
                        top -= 1
        return cnt