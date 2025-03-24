class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        res, today = 0, 0
        for start,end in meetings:
            if today + 1 < start:
                res += start - today - 1
            today = max(today, end)
        res += days - today
        return res
