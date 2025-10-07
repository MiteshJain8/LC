class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        n = len(rains)
        ans = [-1] * n
        sunny_days = SortedList()
        last_rain = {}

        for i, lake in enumerate(rains):
            if lake > 0:
                if lake in last_rain:
                    idx = sunny_days.bisect_right(last_rain[lake])
                    if idx == len(sunny_days):
                        return []
                    dry_day = sunny_days[idx]
                    ans[dry_day] = lake
                    sunny_days.discard(dry_day)
                last_rain[lake] = i
            else:
                sunny_days.add(i)
                ans[i] = 1

        return ans