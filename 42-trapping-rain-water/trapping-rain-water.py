class Solution:
    def trap(self, list1: List[int]) -> int:
        n = len(list1)
        heap = []
        visit = [False] * n
        heappush(heap, (list1[0], 0))
        heappush(heap, (list1[n-1], n-1))
        visit[0], visit[n-1] = True, True
        res = 0
        while heap:
            val, i = heappop(heap)
            if 0 <= i-1 and not visit[i-1]:
                visit[i-1] = True
                res += max(0, val - list1[i-1])
                heappush(heap, (max(val, list1[i-1]), i-1))
            if n > i+1 and not visit[i+1]:
                visit[i+1] = True
                res += max(0, val - list1[i+1])
                heappush(heap, (max(val, list1[i+1]), i+1))

        return res