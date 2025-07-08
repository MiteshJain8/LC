class Solution:
    @lru_cache(maxsize=None)
    def binary_search(self, i):
        return bisect_left(self.events, self.events[i][1] + 1, key=lambda e : e[0])

    @lru_cache(maxsize=None)
    def dp(self, i, k):
        if i >= len(self.events) or k <= 0:
            return 0
        
        skip_value = self.dp(i + 1, k)
        j = self.binary_search(i)
        take_value = self.events[i][2] + self.dp(j, k - 1)
        return max(skip_value, take_value)

    def maxValue(self, events: List[List[int]], k: int) -> int:
        self.events = sorted(events)
        return self.dp(0, k)