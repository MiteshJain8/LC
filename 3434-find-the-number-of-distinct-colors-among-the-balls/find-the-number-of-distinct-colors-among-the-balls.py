class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        ball_color_map = {}
        color_count = defaultdict(int)
        distinct_colors = set()
        res = []
        for x, y in queries:
            if x in ball_color_map:
                old_color = ball_color_map[x]
                color_count[old_color] -= 1
                if color_count[old_color] == 0:
                    del color_count[old_color]
            ball_color_map[x] = y
            color_count[y] += 1
            res.append(len(color_count))
        return res